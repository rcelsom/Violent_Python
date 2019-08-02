import optparse
import socket
from socket import *
from threading import *

screenlock = Semaphore(value=1)

#sends string to tgtHost on tgtPort and outputs if open or closed port
#based on ta
def connScan(tgtHost, tgtPort, openPorts):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('ViolentPython\r\n')
		results = connSkt.recv(100)
		screenlock.acquire()
		print '[+] %d /tcp open' %tgtPort
		print '[+] ' + str(results)
	except:
		screenlock.acquire()
		print '[+] %d /tcp closed' %tgtPort
	finally:
		screenlock.release()
		connSkt.close()

#tries to resolve host name, then calls connScan in threaded form 
def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s': Unknown Host" %tgtHost
		return
		
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '\n[+] Scan Results For: ' + tgtName[0]
	except:
		print '\n[+] Scan Results Fot: ' + tgtIP
		
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target = connScan, args = (tgtHost, int(tgtPort)))
		t.start()
    openPorts[]
			
def main():
	parser = optparse.OptionParser("usage%prog "+\
		"-H <target host> -p <target port>")
		
	parser.add_option("-H", dest = 'tgtHost', type = 'string',\
		help = 'specify target host')
	parser.add_option("-p", dest = "tgtPort", type='string',\
		help = 'specify target port(s) seperated by commas')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts == None):
		print parser.usage
		exit(0)
	
	portScan(tgtHost, tgtPorts)
	
if __name__ == '__main__':
	main()
		