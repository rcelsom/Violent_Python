#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:39:27 2019

@author: rcelsom

Description: searches and stores metadata from some image files
using exiftool for image info, and BeatifulSoup for downloading
images
"""


import urllib2
import optparse
from urlparse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

def findImages(url)::
    print '[+] Finding images on '+url
    urlContent = urllub2.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

def downloadImage(imgTag):
    try:
        print('[+] Downloading image...')
        imgSrc = imgTag['src']
        imgContent = urllib2.urlopen(imgSrc).read()
        imgFileName = basenam(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''
    
def testForExit(imgFlieName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print '[*] ' + imgFileName + \
                    ' contains GPS metadata'
    except:
        pass
    
def main():
    parser = optparse.OptionParser('usage%prog '+ \
                                   '-u <target url>')
    parser.add_option('-u', dest = 'url', type = 'string',
                      help = 'specify url address')
    (options, args) = parser.parse_args()
    url = options.url        
    if url == None:
        print (parser.usage)
        exit(0)
    else:
        imgTages = findImages(url)
        fir imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
            testForExif(imgFileName)
            
if __name__ == '__main__':
    main()
        
    


