#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/19

@summary: 

@author: huxiufeng
'''
import urllib
import urllib2
import cookielib
import zlib
import re
import bz2
import httplib

def getcookie(sites, names, cookiefile):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    login_path = sites
    
    data = names
    #post_data = urllib.urlencode(data)
    #request = urllib2.Request(login_path)
    
    try :
        htmlop = opener.open(login_path)
        html = htmlop.read()
    except urllib2.HTTPError as http_error:
        print http_error.read()
        #print zlib.decompress(http_error.read(), 30)
    if cj :
        print cj
    #cj.save(cookiefile)



    
def getUrl(urlori, ck):
    page = urllib2.urlopen(urlori, timeout = 10)
    data = page.read()
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.open(urlori).read()
    print "cj is ", str(cj)
    patten = r'info=(\S+)'
    cmp = re.compile(patten)
    dt = cmp.findall(str(cj))
    if len(dt) > 0:
        print "dt ",dt
        ck +=dt[0]
        print "cj", dt[0]
    print "data is ", data
    return data, ck

def getnum(data):
    patten = r'(\d+)$'
    cmp = re.compile(patten)
    idx = cmp.findall(data)
    if len(idx) > 0 :
        num = idx[0]
        print "startid is ", num
        return num
    return None


def geturlloop(baseurl, startid):
    ck = ''
    while True :
        data, ck = getUrl(baseurl+str(startid),ck)
        startid = getnum(data)
        if startid is None :
            break
    print "ck is ",ck
    info=urllib.unquote_plus(ck)
    print info
    ckbz = bz2.decompress(info)
    print ckbz
    
    
def putcookie():
    h={}
    h['cookie']='info='+urllib.quote_plus('the flowers are on their way')
    conn=httplib.HTTPConnection('www.pythonchallenge.com')
    conn.set_debuglevel(1)
    conn.request('GET','http://www.pythonchallenge.com/pc/stuff/violin.php',headers=h)
    res=conn.getresponse()
    print res.read() 

#----------------------It is a split line--------------------------------------

def main():
#    sites = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345'
#    names = {'name':'huge', 'passwd':'file'}
#    cookiefile = r'res/p17.txt'
#    getcookie(sites, names, cookiefile)
#    
#    baseurl = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
#    startid = '12345'
#    geturlloop(baseurl, startid)
    
    putcookie()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"