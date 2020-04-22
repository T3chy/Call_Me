from bs4 import BeautifulSoup
import requests
import re
import pandas
import os
def gettranscriptlinks(ticker):
    links = []
    request = requests.get('http://www.conferencecalltranscripts.org/?co=' + ticker)
    soup = BeautifulSoup(request.text,'html.parser')
    transcripts = soup.findAll('div',"tab-pane active")
    transcripts = transcripts[0].findAll('a')
    for i in transcripts:
        links.append([i.get_text(),(re.search('location=(.*)',i['href']).group(0).strip('location='))])
    return([ticker,links])
def downloadtranscripts(links):
    try:
        os.mkdir(links[0])
        os.chdir(links[0])
    except OSError:
        os.chdir(links[0])
    for i in range(10):
        with open(links[1][i+1][0] + '.txt','w') as f:
            f.write(requests.get(links[1][i+1][1]).text)
downloadtranscripts(gettranscriptlinks('TSLA'))