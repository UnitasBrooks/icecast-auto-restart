import urllib2
import time
import subprocess
from bs4 import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup
#'http://www.diliak.net:8000'
soup = BeautifulSoup(urllib2.urlopen('http://stream.kpsu.org:8080/').read())

while True:
	try:
		soup = BeautifulSoup(urllib2.urlopen('http://stream.kpsu.org:8080/').read())
		j = soup.findAll('table')[1] # if the mount point is active this will be fine
	except IndexError:
		subprocess.call(['./test.sh']) # other wise the mount point has failed
		print "stream failed, restarting"
		time.sleep(900)
	print "stream is fine"
	time.sleep(900) # check every 15 minutes	
