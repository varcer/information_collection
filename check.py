# -*- coding: utf-8 -*-
# @Author:varcer
from splinter import Browser
import re
def dump_data(url):#ip反查数据获取
    data=[]
    url = 'http://webscan.360.cn/index/checkwebsite/?url=%s'%url
    browser=Browser('chrome',headless=True)
    browser.visit(url)
    html=browser.html
    d1=re.compile('<h4><strong>(漏洞时间：\d+.+)</strong></h4>').findall(html)
    d2 = re.compile('<li.{0,50}>高危漏洞<span.{0,50}>(\d+)</span>个页面</li>').findall(html)
    d3 = re.compile('<li.{0,50}>严重漏洞<span.{0,50}>(\d+)</span>个页面</li>').findall(html)
    d4 = re.compile('<li.{0,50}>警告漏洞<span.{0,50}>(\d+)</span>个页面</li>').findall(html)
    d5 = re.compile('<li.{0,50}>轻微漏洞<span.{0,50}>(\d+)</span>个页面</li>').findall(html)
    data.append(d1[0])
    data.append('高危漏洞' + d2[0] + ' 个页面')
    data.append('严重漏洞' + d3[0] + ' 个页面')
    data.append('警告漏洞' + d4[0] + ' 个页面')
    data.append('轻微漏洞' + d5[0] + ' 个页面')
    return data