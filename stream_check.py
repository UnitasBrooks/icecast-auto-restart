import urllib2
import time
import subprocess
from bs4 import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup
#'http://www.diliak.net:8000'

while True:
	try:
		soup = BeautifulSoup(urllib2.urlopen('http://stream.kpsu.org:8080/').read())
		j = soup.findAll('table')[2] # if the mount point is active this will be fine
	except IndexError:
		print "stream failed, restarting" # otherwise the mount point has faileds
		subprocess.call(['./test.sh']) 
		time.sleep(900)
	print "stream is fine"
	time.sleep(120) # check every 2 minutes	
