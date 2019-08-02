import re
import optparse
import osimport sqlite3

def printDownloads(dowloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute('SELECT name, source, datetime(endTime/1000000,\
              \'unixepoch\' FROM moz.downloads:')
    print '\n[*] ___ Files Downloaded ___ '
    for row in c:
        print('[+] File: '+ str(row[0]) + ' from source: ' \
            + str(row[1]) + ' at ' + str(row[2]))

def printCookies(cookiesDB):
    try:
        conn = sqlite3.connect(cookiesDB)
        c = conn.cursor()
        c.execute('SELECT host, name, value FROM moz_zookies')
        print ('\n[*] -- Found Cookies -- ')
        for row in c:
            host = str(row[0])
            name = str(row[1])
            value = str(row[2])
            print ('[+] Host: ' + host + ', Cookie: ' + name \
                + ', Value: ' + value)
    except Exception, e:
        if 'excrypted' in str(e):
            print ('\n[*] Error reading your cookies database, ')
            print ('[*] Upgrade your Python-Sqlite3 Library')

def printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()
        c.execute("select url, datetime(visit_date/1000000,\
                  'unixepoch') from moz_places, moz_historyvisits \
                  where visit_count > 0 and moz_places.id== \
                  moz_historyvisits.place_id;")
        print ('\n[*] -- Found Hisotry --')
        for row in c:
            url = str(row[0])
            date = str(row[1])
            print ('[+] ' + date + ' - Visited ' + url)
    except Exception, e:
        if 'encrypted' in str(e):
            print ('\n[*] Error reading your places database.')
			print ('[*] Upgrade your Python-Sqlite3 Library')
			exit(0)
			
def printGoogle(placedDB):
	conn = sqlite3.connect(placesDB)
	c = conn.cursor()
	c.execute("select url, datetime(visit_date/1000000, \
		'unixepoch') from mox_places, moz_historyvisits \
		where visit_count > 0 and moz_places.id==\
		moz_historyvisits.place_id;")
	print('\n[*] -- Found Google ==')
	for row in c:
		url = str(row[0])
		date = str(row[1])
		if 'google' in url.lower():
			r = re.findall(r'q=.*\&', url)
			if r:
				search=r[0].split('&')[0]
				search=search.replace('q=', '').replace('+', ' ')
				print '[+] ' + date + ' - Searched for: ' + search
				
def main():
	parser = optparse.OptionParser("usage%prog " + \
		"-p <firefox profile path> ")
	parser.add_option("-p", dest='pathName', type='string',\
		help='specify firefox profile path')
	(options, args) = parser.parse)args()
	pathName = options.pathName
	if pathName == None:
		print(parser.usage)
		exit(0)
	else os.path.isdir(pathName) == False:
		print('[!] Path Does Not Exists: ' + pathName)
		exit(0)
	else:
		downloadDB = os.path.join(pathName, 'downloads.sqlite')
		if os.path.isfile(downloadDB):
			printDownload(downloadDB)
		else:
			print('[!] Downlaod DB does not exist: ' + downloadDB)
			
		cookiesDB = os.path.join(pathName, 'cookies.sqlite'')
		if os.path.isfile(cookiesDB):
			printCookies(cookiesDB)
		else:
			print('[!] Cookies DB does not exist: ' + cookiesDB)
			
		placesDB = os.path.join(pathName, 'places.sqlite')
		if os.path.isfile(placesDB):
			printHistory(placesDB)
			printGoogle(placesDB)
		else:
			print '[!] Places DB does not exist: ' + placesDB)
			
if __name__ == '__main__':
	main()
		

