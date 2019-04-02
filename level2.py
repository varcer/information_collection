# -*- coding: utf-8 -*-
# @Author:varcer
from splinter import Browser
def dump_data(url):#ip反查数据获取
    url = 'https://toolbar.netcraft.com/site_report?url=%s'%url
    browser=Browser('chrome',headless=True)
    browser.visit(url)
    value={}
    missage={}
    f = open('./conf/xpath1', 'r')
    key=1
    try:
        for xpath1 in f:
            if 'th' in xpath1:
                for i in range(1,6):
                    name=browser.find_by_xpath(xpath1%str(i)).value
                    missage[i]={name:[]}
            else:
                for k in missage[key].keys():
                    for j in range(1,7):
                        va=browser.find_by_xpath(xpath1%j).value
                        missage[key][k].append(va)
                key+=1
    except:
        pass
    try:
        f.close()
        f = open('./conf/xpath', 'r')
        for xpath in f:
            if len(xpath)>5:
                if 'th' in xpath:
                    name = browser.find_by_xpath(xpath.replace('\n\r', '')).value
                    value[name]=[]
                else:
                    missag= browser.find_by_xpath(xpath.replace('\n\r', '')).value
                    value[name].append(missag)
        f.close()
    except:
        pass
    return value,missage