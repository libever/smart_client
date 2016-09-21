#!/usr/bin/env python
#coding=utf-8

import cookielib
import urllib2
import urllib
from pyquery import PyQuery

class smart_client :

    timeout = 3

    def __init__(self,timeout=3,ua="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",cookie_file="/tmp/default_cookie.txt",cookie_str=False):
        self.cookie_file = cookie_file
        self.global_cookie = cookielib.MozillaCookieJar(self.cookie_file)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.global_cookie))
        self.opener.addheaders = [('User-agent',ua)]
        if cookie_str:
            self.opener.addheaders.append(('Cookie',cookie_str))
        self.timeout = timeout

    def saveCookie(self):
        self.global_cookie.save(ignore_discard=True, ignore_expires=True)

    def openUrl(self,url):
        self.content = self.opener.open(url,timeout=self.timeout).read()
        self.pqdom = PyQuery(self.content)
        return self

    def postUrl(self,url,params):
        request = urllib2.Request(
            url = url,
            data = urllib.urlencode(params),
            #默认请求数据格式
            headers = {"Content-Type":"application/x-www-form-urlencoded"}
        )
        self.content = self.opener.open(request,timeout=self.timeout).read()
        self.pqdom = PyQuery(self.content)
        return self

    def find(self,args):
        return PyQuery(self.pqdom.find(args))

if __name__ == "__main__":
    sc = smart_client()
    print sc.openUrl('https://github.com/').content

