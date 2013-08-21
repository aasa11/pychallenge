#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/19

@summary: 

@author: huxiufeng
'''
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import urllib2,cookielib,re 
cookies=cookielib.CookieJar() 
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies)) 
response=opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php') 
print cookies 

#----------------------It is a split line--------------------------------------

def main():
    pass
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"