#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:39:27 2019

@author: rcelsom

Description: this script gets metadata for pdf files using PyPDF
"""


import PyPDF2
from PyPDF2 import PdfFileReader
import optparse


def printMeta(fileName):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print('[*] PDF Metadata Fot: ' + str(fileName))
    for metaItem in docInfo:
        print ('[+] ' + metaItem + ':' + docInfo[metaItem] )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

def main():
    parser = optparse.OptionParser('usage %prog ' +\
                                   "-F <PDF File Name>")
    parser.add_option('-F', dest = 'fileName', type = 'string',\
                      help = 'specify PDF file name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print (parser.usage)
        exit(0)
    else:
        printMeta(fileName)
        
if __name__ == '__main__':
    main()