from bs4 import BeautifulSoup

import requests
import datetime
ask = raw_input("Enter the URL: ")
cert = raw_input("Does it have a SSL certificate ?(y/n) ")

t1 = datetime.datetime.now()


if cert=="y" or cert=="Y":
	r = requests.get("https://"+ask, verify=False)
else:
	r = requests.get("http://"+ask, verify=False)
data  = r.text

soup = BeautifulSoup(data,"lxml")
count = 0
links = [link for link in soup.find_all('a', href=True)]
for link in links:
	print link.get('href')
	count += 1
t2 = datetime.datetime.now()	
total_time = t2-t1
print "--------------------------------------------------------------"
print "STATSITCS "
print "=============================================================="	
print "Total links found: %d" % count	
print "Total time taken: %s" % total_time