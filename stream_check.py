import urllib2
import time
from datetime import datetime
import subprocess
from bs4 import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup
#'

while True:
	soup = BeautifulSoup(urllib2.urlopen('http://www.diliak.net:8000/').read())
	j = soup.findAll('table')
	if len(j) != 3:
		print "stream failed, restarting" # otherwise the mount point has failed
		subprocess.call(['./test.sh']) 
		text_file = open("stream_failure_log.txt","a")
		text_file.write("stream failed at: ")
		text_file.write(str(datetime.now()))
		text_file.write("\n")
		text_file.close()
		time.sleep(900)
	print "stream is fine"
	time.sleep(120) # check every 2 minutes	
