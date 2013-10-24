import urllib2
import time
from datetime import datetime
import subprocess
from bs4 import BeautifulSoup
# Diliak is a icecast server that at the time I wrote this always failed
# http://www.diliak.net:8000/

def connection_error():
	print "Internet dropped"
	text_file = open("stream_failure_log.txt","a")
	text_file.write("Internet dropped at: ")
	text_file.write(str(datetime.now()))
	text_file.write("\n")
	text_file.close()
	time.sleep(3600)

def stream_dropped():
	print "stream failed, restarting" # otherwise the mount point has failed
	subprocess.call(['./test.sh']) 
	text_file = open("stream_failure_log.txt","a")
	text_file.write("stream failed at: ")
	text_file.write(str(datetime.now()))
	text_file.write("\n")
	text_file.close()
	time.sleep(900)

while True:
	# check internet connection
	try:
		soup = BeautifulSoup(urllib2.urlopen('http://stream.kpsu.org:8080').read())
	except urllib2.URLError:
		connection_error()

	tables = soup.findAll('table') # there should be three tables present, otherwise the stream is down
	if len(tables) != 3:
		stream_dropped()
			
	print "stream is fine"
	print str(datetime.now())
	time.sleep(15) # check every 15 seconds	


