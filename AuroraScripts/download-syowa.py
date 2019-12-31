#!/usr/bin/env python
# coding: utf-8

# In[70]:


import urllib.request
from datetime import datetime, timedelta
import os, time, re
from bs4 import BeautifulSoup, SoupStrainer
import requests
from multiprocessing import Pool
from tqdm import tqdm

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/5                                                                                    37.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}


def download_img(url_address, filename):
    request_ = urllib.request.Request(url_address, None, headers)  # The assembled request
    response = urllib.request.urlopen(request_)  # store the response
    # create a new file and write the image
    f = open(str(filename), 'wb')
    f.write(response.read())
    f.close()


#targetdate = 20150622
baseurl = "http://nordlys.nipr.ac.jp/acaurora/Syowa"


def find_indiv_url(dayurl):
    page = requests.get(dayurl)
    data = page.text
    soup = BeautifulSoup(data, "html.parser")

    indiv_url_list = [baseurl + (link.get('href'))[2:] for link in soup.find_all('a', href=re.compile('.*photo.*'))]
    return indiv_url_list


def getimages(indiv_url,targetdate):
    page = requests.get(indiv_url)
    data = page.text
    soup = BeautifulSoup(data, "html.parser")
    img_baseurl = "http://nordlys.nipr.ac.jp"

    for link in soup.find_all('img'):
        smallimage = img_baseurl + link.get('src')
        bigimage = smallimage[:-5] + ".jpg"
        fname = bigimage.split('/')[-1]
        fpath = "AuroraImages/"+str(targetdate)[0:4]+"/"+str(targetdate) + "/" + fname
        print(bigimage, fpath)
        if not os.path.isfile(fpath):
            download_img(bigimage, fpath)
        else:
            print("Exists, Skipped")


def getimgnum(url):
    req = urllib.request.Request(url, None, headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    num = re.findall(r'cam = new Array\((.*?)\);', str(respData))
    return int(num[0])


def makefolder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        pass


def getdayimages(day):
    # global targetdate
    # targetdate = day
    makefolder("AuroraImages/"+str(day)[0:4]+"/"+str(day))
    dayurl = "http://nordlys.nipr.ac.jp/acaurora/Syowa/html/wrap.php?html=" + str(day) + ".html"
    for url in find_indiv_url(dayurl):
        getimages(url,day)


def get_dates_of_year(year):
    montagedir = "datemontages/"+str(year)
    makefolder("AuroraImages/"+str(year))
    dates= [i.split("-")[0] for i in os.listdir(montagedir)]
    return dates

days = get_dates_of_year(2011)
#days = [20140602, 20140603, 20140628, 20140629, 20140604, 20140605, 20140606, 20130705, 20130706, 20130715, 20131008, 20130317, 20140429, 20140430, 20120424, 20120425, 20120715, 20120716, 20120807, 20120808, 20120902, 20120903, 20120904, 20120905, 20120906, 20110302, 20110303, 20110410, 20110411, 20110730, 20110731, 20110801, 20110926, 20110927, 20110930, 20111001]

#days = [20130715]

if __name__ == '__main__':
    #print (days)
    print(len(days))
    pool = Pool(processes=6)
    pool.map(getdayimages, days)
