#!/usr/bin/env python3

import requests, optparse
from bs4 import BeautifulSoup

def main():
    global options
# Definisco le due variabili sotto e le inizializzo con valori a caso
# Questo perchè se in tutta la pagina non trovo un provvedimento
# allora lastDetermina e allegatoB restano non inizializzate e mandano
# in errore lo script

    global determina
    global lastDetermina
    global allegatoB

    determina = ""
    lastDetermina = "https://www.agcom.it/provvedimenti-a-tutela-del-diritto-d-autore"
    allegatoB = "https://www.example.com"


    # Elaborazione argomenti della linea di comando
    usage = "usage: %prog [options] arg"
    parser = optparse.OptionParser(usage)
    parser.add_option("-o", "--output", dest="out_file", help="File di output generato")

    (options, args) = parser.parse_args()
    if len(args) == 1:
        parser.error("Numero di argomenti non corretto")
    if (options.out_file is None):
        parser.error("Numero di argomenti non corretto")

    url = "https://www.agcom.it/provvedimenti-a-tutela-del-diritto-d-autore"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for div in soup.findAll('div', attrs={'class':'risultato'}):
        for p in div.findAll('p'):
            if "Provvedimento" in p.text:
                determina = div.find(lambda tag:tag.name=="a" and ("Determina" or "Delibera" in tag.text))
                break
            lastDetermina = "https://www.agcom.it"+determina["href"]

    page = requests.get(lastDetermina)
    soup = BeautifulSoup(page.content, "html.parser")
    for allegato in soup.find_all("a"):
        if not "Allegato B" in allegato.text:continue
        allegatoB = allegato["href"]
        break

# Controllo se ho trovato un Allegato B vedendo se la variabile inizializzata è stata modificata
# Solo se allegatoB è stato trovato, allora lo elaboro

    if not "www.example.com" in allegatoB:
        response = requests.get(allegatoB)
        with open(options.out_file,'wb') as f:
            f.write(response.content)

if __name__ == '__main__':
    main()
