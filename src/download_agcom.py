#!/usr/bin/env python3

import requests, optparse, sys
from bs4 import BeautifulSoup

def main():
    global options
    # Definisco le due variabili sotto e le inizializzo nulle
    # Questo perchè se in tutta la pagina non trovo un provvedimento
    # allora lastDetermina e allegatoB restano non inizializzate e mandano
    # in errore lo script

    lastDetermina = None
    allegatoB = None


    # Elaborazione argomenti della linea di comando
    usage = "usage: %prog [options] arg"
    parser = optparse.OptionParser(usage)
    parser.add_option("-o", "--output", dest="out_file", help="File di output generato")

    (options, args) = parser.parse_args()
    if len(args) == 1:
        parser.error("Numero di argomenti non corretto")
    if (options.out_file is None):
        parser.error("Numero di argomenti non corretto")

    #Scarico solo l'ultima Determina dal sito AGCOM

    url = "https://www.agcom.it/provvedimenti-a-tutela-del-diritto-d-autore"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for div in soup.findAll('div', attrs={'class':'risultato'}):
        for p in div.findAll('p'):
            if not ("Provvedimento" in p.text or "Ordine" in p.text):continue
            tag = div.find('a')
            if "Determina" in tag.text:
                lastDetermina = "https://www.agcom.it"+tag["href"]
                break
        if lastDetermina is not None:break

    if lastDetermina is not None:
        page = requests.get(lastDetermina)
        soup = BeautifulSoup(page.content, "html.parser")
        for allegato in soup.find_all("a"):
            if not "Allegato B" in allegato.text:continue
            allegatoB = allegato["href"]
            break
    # Controllo se ho trovato un Allegato B vedendo se la variabile inizializzata è stata modificata
    # Solo se allegatoB è stato trovato, allora lo scrivo nel file di output specificato

    if allegatoB is not None:
        response = requests.get(allegatoB)
        with open(options.out_file,'wb') as f:
            f.write(response.content)
        sys.exit(0)
    else:
        sys.exit(1)
    
    

if __name__ == '__main__':
    main()
