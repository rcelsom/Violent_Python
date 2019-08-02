#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:39:27 2019

@author: rcelsom

Description: this script gets all past connected networks of a windows 
machine and gets the lattitude and longitude of the network using wigle.com.This
allows the attacker to see where the computer has been and what it has connected to.
"""

import os
import optparse
import mechanize
import urllib
import re
import urlparse
from _winreg import *

def val2addr(val):
    addr = ''
    for ch in val:
        addr+= '%02x '% ord(ch)
        
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr

def wiglePrint(username, password, netid):
    browser = mechanize.Browser()
    browser.open('http://wigle.net')
    regData = urllib.urlencodoe({'credential_0': username, 
                                 'credential_l': password})
    browser.open('https://wigle.net//gps/gps/main/login', regData)
    params = {}
    params['netid'] = netid
    reqParams = urllib.urlencode(params)
    respURL = 'http://wigle.net/gps/gps/main/confirmquery/'
    resp = browser.open(respURL, reqParams).read()
    mapLat = 'N/A'
    mapLon = 'N/A'
    rLat = re.findall(r'maplat=.*\&', resp)
    if rLat:
        mapLat = rLat[0].split('&')[0].split('=')[1]
    rLon = re.findall(r'maplon=.*\&', resp)
    if rLon:
        mapLon = rLon[0].split
    print ('[-] Lat: ' + mapLat + ', Lon: ' + mapLon)
    
def printNets(username, password):
    net = \
    "SOFTWARE\\Microsoft\\Windows NT" +\
    "\\CurrentVersion\\NetworkList\\Signatures]Unmanaged"
    
    print('\n[*] Networks you have joined')
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (n, addr, t) = EnumValue(netKey, 5)
            (n, name, t) = EnumValue(netkey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print ('[+] ' + netName + ' ' + macAddr)
            wiglePrint(username, password, macAddr)
            CloseKey(netKey)
        except:
            break

def main():
    parser = optparse.OptionsParser("usage%prog " +\
                                    "-u <wigle username> +\
                                    -p <wigle password>")
    parser.add_option('-u', dest = 'username', type = 'string',
                      help = 'specify wigle password')
    parser.add_option('-p', dest = 'password', type = 'string', 
                      help = 'specift wigle username')
    (options, args) = parser.parse_args()
    username = options.username
    password = options.password
    if username == None or password == None:
        print (parser.usage)
        exit(0)
    else:
        printNets(username, password)
        
if __name__ == '__main__':
    main()
    