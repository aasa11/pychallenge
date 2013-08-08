#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/06

@summary: 

@author: huxiufeng
'''
import urllib2
import pickle


def geturl(urlori):
    page = urllib2.urlopen(urlori, timeout=10)
    data = page.read()
    page.close()
    data2 = pickle.loads(data)
    #print data2
    return data2

def getdata(data):
    for line in data:
        #print line
        print(''.join(map(lambda x: x[0]* x[1], line)))

#----------------------It is a split line--------------------------------------

def main():
    urlori = r'http://www.pythonchallenge.com/pc/def/banner.p'
    data = geturl(urlori)
    
    getdata(data)
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"