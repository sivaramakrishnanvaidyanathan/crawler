__author__ = 'sivvaidyanathan'

from urllib2 import urlopen
from bs4 import BeautifulSoup
import codecs, sys

filename = sys.argv[0]
reader = open(filename, 'r')
writer = codecs.open(filename + "_canonical", 'w', 'utf-8')

for line in reader:

    url = line.strip()
    if url.find("http") == -1:
        url = "http://" + url
    data = urlopen(url).read()
    soup = BeautifulSoup(data)

    links = soup.findAll('link', rel="canonical")

    for link in links:
        writer.write(url + "\t" + link["href"] + "\n")
