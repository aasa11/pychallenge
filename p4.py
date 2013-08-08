#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/06

@summary: 

@author: huxiufeng
'''

import urllib2


def getUrl(urlori):
    page = urllib2.urlopen(urlori, timeout = 10)
    data = page.read()
    print "data is ", data
    return data

def getnum(data):
    patten = r'the next nothing is '
    idx = data.find(patten)
    if idx >= 0 :
        num = data[idx+len(patten):]
        print "startid is ", num
        return num
    return None


def geturlloop(baseurl, startid):
    while True :
        data = getUrl(baseurl+str(startid))
        startid = getnum(data)
        if startid is None :
            break
    
        



#----------------------It is a split line--------------------------------------

def main():
    baseurl = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    startid = '8022'
    geturlloop(baseurl, startid)
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"