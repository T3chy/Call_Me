from bs4 import BeautifulSoup
import requests
import re
def gettranscriptlinks(ticker):
    links = []
    request = requests.get('http://www.conferencecalltranscripts.org/?co=' + ticker)
    soup = BeautifulSoup(request.text,'html.parser')
    transcripts = soup.findAll('div',"tab-pane active")
    transcripts = transcripts[0].findAll('a')
    for i in transcripts:
        links.append([i.get_text(),(re.search('location=(.*)',i['href']).group(0).strip('location='))])
    return(links)
print(gettranscriptlinks('TSLA'))