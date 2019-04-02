# -*- coding: utf-8 -*-
# @Author:varcer
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
import threading
import whois_missage
import subdomain
import level2
import conf
import check
import re
def chec(url):
    data=check.dump_data(url)
    t22=tk.Text(f2,width=25,height=10)
    t22.place(x=0,y=280)
    t22.config(state=DISABLED)
    for i in data:
        t22.config(state=NORMAL)
        t22.insert('end',i+'\n\r')
        t22.config(state=DISABLED)
def level(url):
    win1 = tk.Tk()
    win1.title('level-2')
    sw = win1.winfo_screenwidth()
    sh = win1.winfo_screenheight()
    ww = 800
    wh = 510
    x = (sw - ww) / 2
    y = (sh - wh) / 2
    win1.geometry("%dx%d+%d+%d" % (ww, wh, x-100, y))
    t11 = ScrolledText(win1, height=32, width=97, font=20)
    t11.place(x=0, y=0)
    t11.config(state=NORMAL)
    def start(url):
        t11.config(state=NORMAL)
        t11.insert('end','scanning......')
        t11.config(state=DISABLED)
        value,missage=level2.dump_data(url)
        t11.config(state=NORMAL)
        t11.delete(1.0,END)
        t11.config(state=DISABLED)
        t11.config(state=NORMAL)
        for k in value.keys():
            t11.insert('end',k+' : '+value[k][0]+'\n\r\n\r')
        for i in missage.keys():
            for k in missage[i].keys():
                t11.insert('end', '\n\r'+k+' :\n\r\t')
                for data in missage[i][k]:
                    t11.insert('end',data + '\n\r\t')
        t11.config(state=DISABLED)
    T=threading.Thread(target=start,args=(url,))
    T.start()
    win1.mainloop()


def Go(url):
    url=url
    en1.config(state=NORMAL)
    en1.delete(0,END)
    en1.insert('end','  URL: '+url)
    en1.config(state=DISABLED)
    t.config(state=NORMAL)
    t.delete(1.0, END)
    t.insert('end','whois scanning......')
    t.config(state=DISABLED)
    try:
        missage=whois_missage.get_missage(url)
    except:
        missage={}
    t.config(state=NORMAL)
    t.delete(1.0,END)
    t.config(state=DISABLED)
    for i in missage.keys():
        t.config(state=NORMAL)
        t.insert('end', i+":"'\n\r\n\r')
        t.config(state=DISABLED)
        for j in missage[i]:
            t.config(state=NORMAL)
            t.insert('end',"\t"+j+'\n\r\n\r')
            t.config(state=DISABLED)

def sub(url):
    url=url
    t1.config(state=NORMAL)
    t1.delete(1.0, END)
    t1.insert('end', 'subdomain scanning......')
    t1.config(state=DISABLED)
    try:
        domain=subdomain.subdomain(url)
    except:
        domain={}
    t1.config(state=NORMAL)
    t1.delete(1.0, END)
    t1.insert('end', '子域名:\n\r')
    t1.config(state=DISABLED)
    for i in domain:
        t1.config(state=NORMAL)
        t1.insert('end', '\n\n' + i + '\n\r')
        t1.config(state=DISABLED)

def thread():
    var = en.get()
    if len(var) == 0:
        tkinter.messagebox.showwarning(title='警告', message='URL不能为空')
        return 0
    if "http://" in var or "https://" in var:
        url = var.split('/')[2]
        if 'www.' in url:
            url = url.replace('www.', '')
    else:
        url = var.split('/')[0]
        if 'www.' in url:
            url = url.replace('www.', '')
    temp=url
    if '.' in temp:
        url=temp.split('.')[-2]+'.'+temp.split('.')[-1]
        URL=re.compile('.+\..+').findall(url)
    else:
        tkinter.messagebox.showwarning(title='警告', message='URL不正确')
        return 0
    for t in conf.thread:
        pass
    if var1.get()==1:
        T=threading.Thread(target=Go,args=(url,))
        T.start()
        T1=threading.Thread(target=sub,args=(url,))
        T1.start()
    if var2.get()==1:
        T2=threading.Thread(target=level,args=(url,))
        T2.start()
    if var2.get()==1 or var1.get()==1:
        T3 = threading.Thread(target=chec, args=(url,))
        T3.start()


win=tk.Tk()
win.title('信息收集')
sw = win.winfo_screenwidth()
#得到屏幕宽度
sh = win.winfo_screenheight()
#得到屏幕高度
ww = 800
wh = 510
#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 2
win.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
#win.geometry('800x510')
win.resizable(width=False,height=False)

f0=Frame(win,width=510,height=800)#主frame
f0.pack(ipadx=510,ipady=800)

f1=Frame(f0,width=170,height=105)#log Frame
f1.place(x=0,y=0)
cv=tk.Canvas(f1,bg='green',width=170,height=105)#创建画布
image=tk.PhotoImage(file='./whois/log.PNG')
im=cv.create_image(0,0,anchor='nw',image=image)
cv.pack()

f2=Frame(f0,width=170,height=695)#扫描控制区
f2.place(x=0,y=105)

f3=Frame(f0,width=350,height=695)#结果显示区
f3.place(x=170,y=105)

f4=Frame(f0,width=281,height=695)#漏洞显示区
f4.place(x=519,y=105)

f5=Frame(f0,width=630,height=105)#漏洞显示区
f5.place(x=170,y=0)


b1=tk.Button(f2,text='信息收集',width=8,height=1,font=('Arial',10),command=None)
#b1.place(x=40,y=80)
t=ScrolledText(f3,height=25,width=41,font=20)
t.place(x=0,y=0)
t.config(state=DISABLED)


t1=ScrolledText(f4, height=25, width=32, font=20)
t1.place(x=0, y=0)
t1.config(state=DISABLED)

en=tk.Entry(f5,width=40)
en.place(x=160,y=50)


en1=tk.Entry(f5,width=40,borderwidth=0,state=DISABLED,font='blue')
en1.place(x=160,y=75)

b2=tk.Button(f5,text='Go',width=2,height=1,font=('Arial',10),background='blue',command=thread)
b2.place(x=450,y=48)

var1=tk.IntVar()
var2=tk.IntVar()
ck1=tk.Checkbutton(f2,text='level-1',variable=var1,onvalue=1,offvalue=0,command=None)
ck1.place(x=40,y=80)
ck1=tk.Checkbutton(f2,text='level-2',variable=var2,onvalue=1,offvalue=0,command=None)
ck1.place(x=40,y=120)

win.mainloop()


