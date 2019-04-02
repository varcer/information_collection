# -*- coding: utf-8 -*-
# @Author:varcer
import conf
import os
def get_missage(url1='testfire.net'):
    url=url1
    conf.name.clear()
    conf.adjust_data.clear()
    data=os.popen('whois.exe %s'%url)
    # f=open("./whois/whois.txt",'w')
    # f.write(data.read())
    # f.close()
    conde_name()
    f = data.read().split('\n')
    for j in conf.name.keys():
        for i in f:
            if j in i and len(i)>2:
                temp=i.replace('\n','').strip().split(':',maxsplit=1)
                if temp[1] and 'Not Disclosed' not in temp[1]:
                    if conf.name[j] not in conf.adjust_data.keys():
                        conf.adjust_data[conf.name[j]]=[temp[1]]
                    elif temp[1] not in conf.adjust_data[conf.name[j]]:
                        conf.adjust_data[conf.name[j]].append(temp[1])
        #f.close()
    return conf.adjust_data
def conde_name():#提取名称
    f=open("./whois/conf", 'br')
    for i in f:
        if len(i)>1:
            temp=i.decode('utf-8')
            e_name=temp.split('@')[0]
            c_name = temp.split('@')[1].replace('\r\n','')
            conf.name[e_name]=c_name
    f.close()
def start():
    f=open('./whois/whois.txt','r')
    get_missage(f.read())