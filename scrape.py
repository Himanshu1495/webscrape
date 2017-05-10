from bs4 import BeautifulSoup

import requests
ask = raw_input("Enter the URL: ")
cert = raw_input("Does it have a SSL certificate ?(y/n) ")

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
	
print "Total links visited: %d" % count	