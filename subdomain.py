# -*- coding: utf-8 -*-
# @Author:varcer
from splinter.browser import Browser
import re
def subdomain(url):#ip反查数据获取
    url = 'https://searchdns.netcraft.com/?restriction' \
          '=site+contains&host=%s&lookup=wait..&positi' \
          'on=limited'%url
    browser=Browser('chrome',headless=True)
    browser.visit(url)
    reg=re.compile('<a href="(.+)" rel="nofollow">.{0,9}<font color="#ff0000">.+</font></a>')
    data=reg.findall(browser.html)
    return data