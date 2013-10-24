import urllib2
import time
from datetime import datetime
import subprocess
from bs4 import BeautifulSoup
# Diliak is a icecast server that at the time I wrote this always failed
# http://www.diliak.net:8000/
while True:
	soup = BeautifulSoup(urllib2.urlopen('http://stream.kpsu.org:8080').read())
	tables = soup.findAll('table') # there should be three tables present, otherwise the stream is down
	if len(tables) != 3:
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
