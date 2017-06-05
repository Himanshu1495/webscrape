from bs4 import BeautifulSoup

import requests
import datetime

def traverse(links,already_crawled,count):
	if len(links) != 0:
		for link in links:
			if link not in already_crawled:
				visiting_link = link.get('href')
				if visiting_link.startswith("https://") or visiting_link.startswith("http://"):
					print "Crawling link : %s " % visiting_link
					crawl(visiting_link,links)
					count += 1
				else:
					visiting_link = url + visiting_link
					print "Crawling link : %s " % visiting_link
					crawl(link,links)
					count += 1	

def crawl(link,links):
	already_crawled.append(link)
	r = requests.get(link, verify=False)
	data = r.text
	soup = BeautifulSoup(data, "lxml")
	new_links = [new_find for new_find in soup.find_all('a', href=True)]
	links = links + new_links
	

ask = raw_input("Enter the URL: ")
cert = raw_input("Does it have a SSL certificate ?(y/n) ")

t1 = datetime.datetime.now()


if cert=="y" or cert=="Y":
	pre = "https://"
	url = "https://"+ask
	r = requests.get(url, verify=False)
else:
	pre = "http://"
	url = "http://"+ask
	r = requests.get(url, verify=False)

data  = r.text


soup = BeautifulSoup(data,"lxml")
count = 0
visited = 0
already_crawled = []
links = [link for link in soup.find_all('a', href=True)]
traverse(links,already_crawled,count)

t2 = datetime.datetime.now()	
total_time = t2-t1
print "--------------------------------------------------------------"
print "STATSITCS "
print "=============================================================="	
print "Total links found: %d" % count
print "Total links visited by crawlers : %d " % visited	
print "Total time taken: %s" % total_time