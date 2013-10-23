import urllib2
import time
import subprocess
from bs4 import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://stream.kpsu.org:8080/').read())

j = soup.findAll('table')[2]
print j
while True:
	if j is not None: 
		print "stream is fine"
	else:
		subprocess.call(['./test.sh'])
		print "stream failed, restarting"
		time.sleep(900)
	time.sleep(2)
