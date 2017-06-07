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
					count += 1
					crawl(visiting_link,links)					
				else:
					#if link does not have http:// or https://, prefix it before crawling
					visiting_link = url + visiting_link
					print "Crawling link : %s " % visiting_link
					count += 1
					crawl(link,links)	

def crawl(link,links):
	try:
		r = requests.get(link, verify=True)
		data = r.text
		soup = BeautifulSoup(data, "lxml")
		already_crawled.append(link)
		new_links = [new_find for new_find in soup.find_all('a', href=True)]
		#add new found links to previous links list 
		links = links + new_links
	except:
		not_crawled.append(link)
	
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
#initialise not visited
not_crawled = []
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
print "Total links found: %d" % len(links)
print "Total links visited by crawlers : %d " % len(already_crawled)	
print "Total links not visited by crawlers : %d" % len(not_crawled)
print "Total time taken : %s" % total_time