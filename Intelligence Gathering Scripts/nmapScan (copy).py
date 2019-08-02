import nmap
import optparse
import sys
import time

def nmapScan(tgtHost, tgtPort):
    nm = nmap.PortScanner()

    nm.scan(tgtHost, tgtPort)
    state=nm[tgtHost]['tcp'][int(tgtPort)]['state']
    sys.stdout.write('\033[F')	
    sys.stdout.write('\033[K')
    print " [*] " + tgtHost + ' tcp/'+ tgtPort + ' ' + state + '\n'
		
	
def main():
    parser = optparse.OptionParser("usage%prog "+\
		"-H <target host> -p <target port> -r <lowest port, highest port>")
		
    parser.add_option("-H", dest = 'tgtHost', type = 'string',\
		help = 'specify target host')
    parser.add_option("-p", dest = "tgtPort", type='string',\
		help = 'specify target port(s) seperated by commas')
    parser.add_option("-r", dest = 'tgtPortRange', type = 'string',\
                help = 'specify target range seperated by a comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    tgtPortRange = str(options.tgtPortRange).split(',')
    print(tgtHost, "   ", tgtPorts,"   ", tgtPortRange)
    if (tgtHost == None) or (tgtPorts == None or tgtPortRange[0] == None):
	print (parser.usage)
        exit(0)
		


    if (tgtPorts != None):
        print('tst')
        for tgtPort in tgtPorts:
            nmapScan(tgtHost, tgtPort)
    elif (tgtPortRange != None):
        for i in range(int(tgtPortRange[0]), int(tgtPortRange[1]) + 1):
            nmapScan(tgtHost, str(i))
		
if __name__ == '__main__':
	main()
