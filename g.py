#!/usr/bin/env python
#coding=utf-8

import sys
import smart_client


def simpleTest():
    sc = smart_client.smart_client(timeout=3,cookie_file="a.cookie")
    #token = sc.openUrl("https://github.com/").find("input[name=authenticity_token]").attr("value")
    #sc.saveCookie()
    #params = {
    #    "authenticity_token"        :   token,
    #    "commit"                    :   "Sign in",
    #    "login"                     :   "qixingyue@126.com",
    #    "password"                  :   "123456abc",
    #    "utf8"                      :   "✓"
    #}
    #sc.postUrl("https://github.com/session",params)
    #sc.saveCookie()
    content = sc.openUrl("http://www.runchina.org.cn/portal.php?mod=calendar&ac=list").content
    print content

if __name__ == "__main__":
    argc = len(sys.argv)
    simpleTest()
