import urllib2
import time
from datetime import datetime
import subprocess
from bs4 import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup
#'

while True:
	try:
		soup = BeautifulSoup(urllib2.urlopen('http://stream.kpsu.org:8080').read())
		j = soup.findAll('table')[2] # if the mount point is active this will be fine
	except IndexError:
		print "stream failed, restarting" # otherwise the mount point has faileds
		subprocess.call(['./test.sh']) 
		text_file = open("stream_failure_log.txt","w")
		text_file.write("stream failed at: ")
		text_file.write(str(datetime.now()))
		text_file.close()
		time.sleep(900)
	print "stream is fine"
	time.sleep(120) # check every 2 minutes	
