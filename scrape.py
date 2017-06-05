from bs4 import BeautifulSoup

import requests
import datetime

def traverse(links,already_crawled,count):
	#check if links are present
	if len(links) != 0:
		for link in links:
			#check if link is not already crawled
			if link not in already_crawled:
				visiting_link = link.get('href')
				#if link has http:// or https://
				if visiting_link.startswith("https://") or visiting_link.startswith("http://"):
					print "Crawling link : %s " % visiting_link
					#crawl link
					crawl(visiting_link,links)
					count += 1
				else:
					#if link does not have http:// or https://, prefix it before crawling
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
	#add new found links to previous links list 
	links = links + new_links
	
#ask for url
ask = raw_input("Enter the URL: ")
#ask for SSL Certificate
cert = raw_input("Does it have a SSL certificate ?(y/n) ")

#start the clock for statistics
t1 = datetime.datetime.now()

#if SSL is present 
if cert=="y" or cert=="Y":
	pre = "https://"
	url = "https://"+ask
	r = requests.get(url, verify=False)
#if SSL is not present
else:
	pre = "http://"
	url = "http://"+ask
	r = requests.get(url, verify=False)

#get the source of the page
data  = r.text


soup = BeautifulSoup(data,"lxml")
#initialise count
count = 0
#initialise visited
visited = 0
#initialise already visited
already_crawled = []
#get all links of the page 
links = [link for link in soup.find_all('a', href=True)]
#call traverse function
traverse(links,already_crawled,count)

#get the clock time at end
t2 = datetime.datetime.now()
#calculate total time of the crawl	
total_time = t2-t1
print "--------------------------------------------------------------"
print "STATSITCS "
print "=============================================================="	
print "Total links found: %d" % count
print "Total links visited by crawlers : %d " % visited	
print "Total time taken: %s" % total_time