#!/usr/bin/env python
import os.path, os
import sys


def iterateDirectories(path, subdirs):

    for subdir in subdirs:
        print path + subdir
        listing = os.listdir(path + subdir)
        print listing
        #parseSubDirectory(listing)

def parseSubDirectory(listing):

    d1 = {}

    for infile in listing:
    
        fileName = path + infile
        # print "**** " + fileName

        f = open(fileName, 'rb')
    
        # parse squid proxy secret number from cache file
        #   - in squid cache file, key is offset 0x0a - 0x19 of file
        line1 = ""
        
        index = 0
    
        # read up to the beginning of the URI in the squid cache entry
        while  index < 0x3c:
            line1 = line1 + str(f.read(8))
            index = index + 1
    
        key = line1[0x0a:0x19]
        
        url = ""
        stop = 0 
    
        # parse out URI from squid proxy cache header data
        while line1[index].encode("hex") != "00":
            # print str(index) + " " + url
            line1 = line1 + str(f.read(8))    
            url = url + line1[index]
            index = index + 1
            #print url
    
        # print fileName + " " + key.encode("hex") + " " + url

        d1[str(key.encode("hex"))] = [fileName, url]

    for key, item in d1.items():
        print key, item


if __name__ == "__main__":

    path = sys.argv[1]

    listing = os.listdir(path)
    iterateDirectories(path, listing)
    # parseSubDirectory(listing)

