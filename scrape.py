from bs4 import BeautifulSoup

import requests
import urllib2
import datetime
import re

def traverse(links,already_crawled,count):
	#check if links are present
	if len(links) != 0:
		for link in links:
			#check if link is not already crawled
			if link not in already_crawled:
				visiting_link = link
				#if link has http:// or https://
				if visiting_link.startswith("https://") or visiting_link.startswith("http://"):
					print "Crawling link : %s " % visiting_link
					#crawl link
					crawl(visiting_link,links)					
				else:
					#if link does not have http:// or https://, prefix it before crawling
					visiting_link = url + visiting_link
					print "Crawling link : %s " % visiting_link
					#crawl link
					crawl(link,links)	

def crawl(link,links):
	try:
		r = urllib2.urlopen(link)
		soup = BeautifulSoup(r, 'html.parser')
		already_crawled.append(link)
		new_links = [new_find for new_find in soup.findAll('a', attrs = {'href': re.compile("^"+pre)})]
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
	r = urllib2.urlopen(url)
#if SSL is not present
else:
	pre = "http://"
	url = "http://"+ask
	r = urllib2.urlopen(url)

#get the source of the page
soup = BeautifulSoup(r,'html.parser')


#initialise count
count = 0
#initialise visited
visited = 0
#initialise already visited
already_crawled = []
#get all links of the page 
#initialise not visited
not_crawled = []
links = [link.get('href') for link in soup.findAll('a', attrs = {'href': re.compile("^"+pre)})]
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
for l in not_crawled:
	print l
print "Total time taken : %s" % total_time