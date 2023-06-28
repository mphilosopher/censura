#!/usr/bin/env python3

import requests, optparse, sys
from bs4 import BeautifulSoup

def main():
    global options
    # Definisco le due variabili sotto e le inizializzo nulle
    # Questo perchè se in tutta la pagina non trovo un provvedimento
    # allora lastDelibera e allegatoB restano non inizializzate e mandano
    # in errore lo script

    lastDelibera = None
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

    #Scarico solo l'ultima Delibera dal sito AGCOM
    curPage = 1
    while((allegatoB is None) and (curPage <= 10)):
        url = "https://www.agcom.it/provvedimenti-a-tutela-del-diritto-d-autore?p_p_id=listapersconform_WAR_agcomlistsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_listapersconform_WAR_agcomlistsportlet_numpagris=10&_listapersconform_WAR_agcomlistsportlet_curpagris={}".format(curPage)
        print(curPage)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        for div in soup.findAll('div', attrs={'class':'risultato'}):
            for p in div.findAll('p'):
                if not ("provvedimento" in p.text.lower() or "ordine" in p.text.lower()):continue
                tag = div.find('a')
                if "delibera" in tag.text.lower():
                    lastDelibera = "https://www.agcom.it"+tag["href"]
                    break
            if lastDelibera is not None:break
        

        if lastDelibera is not None:
            page = requests.get(lastDelibera)
            soup = BeautifulSoup(page.content, "html.parser")
            for allegato in soup.find_all("a"):
                if not "allegato b" in allegato.text.lower():continue
                allegatoB = allegato["href"]
                break
        curPage = curPage + 1
        
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
