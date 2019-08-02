#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 06:27:06 2019

@author: rcelsom
"""

import pxssh

def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before

def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print ('[-] Error Connecting')
        exit(0)
        
s=connect('127.0.0.1', 'root', 'toor')
send_command(s, 'cat /etc/shadow | grep root')