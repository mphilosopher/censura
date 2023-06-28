#!/usr/bin/env python3

import requests, optparse
from bs4 import BeautifulSoup

def main():
    global options
# Definisco le tre variabili sotto e le inizializzo con valori a caso
# Questo perchè se in tutta la pagina non trovo un provvedimento
# allora determina,lastDetermina e allegatoB restano non inizializzate e mandano
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

    curpage=1
    lastDetermina = None
    while((curpage<10) and (lastDetermina is None)):        
        url = "https://www.agcom.it/provvedimenti-a-tutela-del-diritto-d-autore?p_p_id=listapersconform_WAR_agcomlistsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_listapersconform_WAR_agcomlistsportlet_numpagris=50&_listapersconform_WAR_agcomlistsportlet_curpagris={}".format(curpage)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        for div in soup.findAll('div', attrs={'class':'risultato'}):
            if lastDetermina: break
            for p in div.findAll('p'):
                if ((p.text.lower().find("provvedimento")==-1) and (p.text.lower().find("ordine")==-1)):continue
                    #determina = div.find(lambda tag:(tag.name=="a" and (tag.text.lower().find("determina")!=-1) or (tag.text.lower().find("delibera")!=-1)))
                determina = div.find(lambda tag:(tag.name=="a" and tag.text.lower().find("determina")!=-1))
                if determina:
                    lastDetermina = "https://www.agcom.it"+determina["href"]
                    #### Check Allegato ######
                    page = requests.get(lastDetermina)
                    soup = BeautifulSoup(page.content, "html.parser")
                    # Controllo se ho trovato un Allegato B vedendo se la variabile inizializzata è stata modificata
                    # Solo se allegatoB è stato trovato, allora lo elaboro
                    for allegato in soup.find_all("a"):
                        if not "Allegato B" in allegato.text:continue
                        allegatoB = allegato["href"]
                        break
                    if not "www.example.com" in allegatoB:
                        response = requests.get(allegatoB)
                        with open(options.out_file,'wb') as f:
                            f.write(response.content)
                    else:
                        lastDetermina = None
                    break
        curpage = curpage + 1
    if lastDetermina is None:
        return(False)

if __name__ == '__main__':
    main()
