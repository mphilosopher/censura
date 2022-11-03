#!/usr/bin/env python3

import requests, optparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


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

    service = Service(executable_path=ChromeDriverManager().install())
    op = webdriver.ChromeOptions()
    op.add_argument('--headless')
    url = "https://www.agcom.it/provvedimenti-a-tutela-del-diritto-d-autore"
    driver = webdriver.Chrome(service=service, options=op)
    driver.get(url)
    lastDetermina = driver.find_element(By.PARTIAL_LINK_TEXT, "Determina").get_attribute('href')
    driver.get(lastDetermina)
    allegatoB = driver.find_element(By.LINK_TEXT, "Allegato B").get_attribute('href')
    driver.quit()

    response = requests.get(allegatoB)
    with open(options.out_file,'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    main()