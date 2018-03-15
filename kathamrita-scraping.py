# -*- coding: utf-8 -*-
import bs4
import requests
import re


url = "https://www.ramakrishnavivekananda.info/kathamrita/unicodekathamrita/01_biography_1_7.html"

def getContent(url):
    html_doc = requests.get(url).content
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    text =  soup.prettify(encoding='UTF-8')
    wordList = text.splitlines()

    textClean = re.sub('<br/>','\n',  str.join(' ', wordList))
    #print textClean

    soup = bs4.BeautifulSoup(textClean, 'html.parser')
    nextPage = soup.findAll('a')[-1]['href']
    pageContent = re.sub(" +" , " ", soup.get_text())

    return (pageContent, nextPage)

pageContent, nextPage = getContent(url)

while nextPage:
    url = "https://www.ramakrishnavivekananda.info/kathamrita/unicodekathamrita/" + nextPage
    pageContent, nextPage = getContent(url)
    print pageContent
    file.write(open("test.txt", 'a'), pageContent.encode('utf-8'))