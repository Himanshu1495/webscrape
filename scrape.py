from bs4 import BeautifulSoup

import requests
import datetime
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
links = []
traverse(soup,url)
def crawl(link):
	r = requests.get(link, verify=False)
	data = r.text
	soup = BeautifulSoup(data, "lxml")
	

def add_links(link):
	if link.startswith("https://") or link.startswith("http://"):
		#do something 
	else:
		links.append(pre+link)


def traverse(soup,url):
	links = [link for link in soup.find_all('a', href=True)]
	for link in links:
		print "Crawling link : %s " % link.get('href')
		add_links(link)
		count += 1



t2 = datetime.datetime.now()	
total_time = t2-t1
print "--------------------------------------------------------------"
print "STATSITCS "
print "=============================================================="	
print "Total links found: %d" % count
print "Total links visited by crawlers : %d " % visited	
print "Total time taken: %s" % total_time