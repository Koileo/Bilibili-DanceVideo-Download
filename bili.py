#!/usr/bin/python
#coding=utf-8
import  xml.dom.minidom
import urllib.request
import sys
from you_get import common as you_get
import time
import os.path
#获得当前系统时间的字符串
localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print('localtime='+localtime)
month=time.strftime('%m',time.localtime(time.time()))
day=time.strftime('%d',time.localtime(time.time()))
os.makedirs('/bilibili/video/2021' + '/'+ str(month) + '/' +  str(day))
directory = '/bilibili/video/2021' + '/'+ str(month) + '/' +  str(day)
url = 'http://rss.koileo.com:1200/bilibili/partion/ranking/20/7'
urllib.request.urlretrieve(url, 'abc.xml')

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement
file = open('link.txt','w')
cc=dom.getElementsByTagName('link')
i=1
while i<=20:
    c=cc[i]
    print(c.firstChild.data)
    print('Top' +str(i)+' ! ! ! ')
    sys.argv = ['you-get','-o',directory,c.firstChild.data]    
    you_get.main()
    i+=1

