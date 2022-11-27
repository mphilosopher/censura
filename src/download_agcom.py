#!/usr/bin/env python3

import requests, optparse
from bs4 import BeautifulSoup

def main():
    global options

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
                lastDetermina = "https://www.agcom.it"+determina["href"]
                break
    page = requests.get(lastDetermina)
    soup = BeautifulSoup(page.content, "html.parser")
    for allegato in soup.find_all("a"):
        if not "Allegato B" in allegato.text:continue
        allegatoB = allegato["href"]
        break

    response = requests.get(allegatoB)
    with open(options.out_file,'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    main()