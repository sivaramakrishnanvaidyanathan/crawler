__author__ = 'sivvaidyanathan'
from bs4 import BeautifulSoup
import requests, sys, json

def crawl(wiki_url):
    response = requests.post(url= wiki_url)
    numLinksToCrawl = 0

    if response.status_code == 200:
        response_html = response.text
        soup = BeautifulSoup(response_html)
        paras = soup.find_all("p")
        for para in paras:
            links = para.find_all("a")
            for link in links:
                try:
                    data = json.dumps({"href":link["href"], "title": link["title"]})
                    print data
                    numLinksToCrawl += 1
                except:
                    print "non crawlable: " + link

    print "numLinksToCrawl: " + str(numLinksToCrawl)








