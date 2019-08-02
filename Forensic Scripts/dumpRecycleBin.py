#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:39:27 2019

@author: rcelsom

Description: this script gets all files in recycle bin on a windows machine
"""

import os
import optparse
from _winreg import *

def sid2user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,
                      "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion" +\
                      "\\ProfileList" + '\\' + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user. value.split('\\')[-1]
        return user
    except:
        return sid
        
#checks for recycle bin dir for windows systems from Windows98
#through Windows 10
#Recycler = Windows NT, 2000, XP - NTFS file system
#Recycled = Windows 98 and prior - FAT file system
#$Recycle.Bin = Windows Vista and After - NTFS file system
def returnDir():
    dirs=['C:\\$Recycle.Bin\\', 'C:\\Recycler', 'C:\\Recycled']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files = os.listdir(recycleDir + sid)
        user = sid2user(sid)
        print ('\n[*] Listing Files from User: ' + str(user))
        for file in files:
            print ('[+] Found File: ' | str(file))
            
def main():
    recycleDir = returnDir()
    findRecycled(recycleDir)
    
if __name__ = '__main__':
    main()
        
    


