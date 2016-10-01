__author__ = 'sivvaidyanathan'
from bs4 import BeautifulSoup
import requests, sys, json

def crawl(wiki_url):
    response = requests.post(url= wiki_url)
    numLinksToCrawl = 0
    crawl_data = []

    if response.status_code == 200:
        response_html = response.text
        soup = BeautifulSoup(response_html)
        paras = soup.find_all("p")
        for para in paras:
            links = para.find_all("a")
            for link in links:
                try:
                    data = json.dumps({"href":link["href"], "title": link["title"]})
                    crawl_data.append(data)
                    print data
                    numLinksToCrawl += 1
                except:
                    print "non crawlable: " + str(link)

    print "numLinksToCrawl: " + str(numLinksToCrawl)
    print "crawl_data\n"
    for crawl_link in crawl_data:
        print "crawl_link: " + crawl_link








