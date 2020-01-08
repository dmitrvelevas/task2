from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import sys
import time

group1 = []
group2 = []
group3 = []
all_links = set()
glob = 'https://www.foxnews.com'
first_article = 'https://www.foxnews.com/politics'


def html_output(triple_list, filename):
    f = open((filename + '.html'), 'w')
    f.write('<HTML><HEAD><META http-equiv="Content-Type" content="text/html; charset=windows-1251"><TITLE>' + filename + '</TITLE></HEAD><BODY>')
    f.write('<h1>' + filename + ' (' + str(len(triple_list)) + ')</h1>')
    for i in triple_list:
        f.write('<p><b>' + i[0] + '</b></p>')
        f.write('<p>Автор: ' + i[1] + '</p>')
        f.write('<a href="' + i[2] + '">' + i[2] + '</a></t></t>')
    f.write('</BODY></HTML>')
    f.close()

for times in range(96,1,-1):
    req = Request(first_article)
    web_page = urlopen(req)
    html_doc = web_page.read()
    soup = BeautifulSoup(html_doc, "html.parser")
    abzac = soup.find('div', {"class": "content article-list"})
    print (times)

    articles = abzac.find_all('a')

    for link in articles:
        word = link.get('href')
        if (word[0:4] != 'http') and (word[0:4] == '/pol') and (word not in all_links):
            all_links.add(word)
            try:
                req_local = Request(glob + word)
                web_page_local = urlopen(req_local)
                html_doc_local = web_page_local.read()
                soup_local = BeautifulSoup(html_doc_local, "html.parser")
            except:
                continue

            try:
                body = str((soup_local.find('div', {"class": "article-body"})).find_all('p'))
            except:
                continue
            if (('Republican' or 'republican') in body):
                group1.append([soup_local.find('h1', {"class": "headline"}).text,
                               (soup_local.find('div', {"class": "author-byline"})).find('a').text,
                              glob+word])
            elif (('Democratic' or 'democratic') in body):
                group2.append([soup_local.find('h1', {"class": "headline"}).text,
                               (soup_local.find('div', {"class": "author-byline"})).find('a').text,
                              glob+word])
            elif ((('Democratic' or 'democratic') and ('Democratic' or 'democratic')) or true in body):
                group3.append([soup_local.find('h1', {"class": "headline"}).text,
                               (soup_local.find('div', {"class": "author-byline"})).find('a').text,
                              glob+word])
    html_output(group1, 'Republican')
    html_output(group2, 'Democratic')
    html_output(group3, 'Остальные')
    time.sleep(900)


    




    

                
