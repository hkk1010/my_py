# !/usr/bin/python
# coding:utf-8

from bs4 import BeautifulSoup
import urllib.request
import re

url = "http://testmall.feiersmart.com/"
resp=urllib.request.urlopen(url)
html = resp.read()
html = html.decode('UTF-8')
bs = BeautifulSoup(html,"html.parser")

data=bs.find('main',id='app')
lis = data.select("div[class_=home-wrapper]")
for x in lis:
    theater = x.find('div', class_='placename')
    print (theater.text)

exit()
k=[]
s = []
sp = []
si = []
for i in k :
    if (re.match(r'src',i) or re.match(r'href',i)):
        if (not re.match(r'href="#"',i)):
            if (re.match(r'.*?png"',i) or re.match(r'.*?ico"',i)):
                if (re.match(r'src',i)):
                    s.append(i)

for it in s :
    if (re.match(r'.*?png"',it)):
        sp.append(it)

cnt = 0
cou = 1
for it in sp:
    m = re.search(r'src="(.*?)"',it)
    iturl = m.group(1)
    print(iturl)
    if (iturl[0]=='/'):
        continue;
    web = urllib.request.urlopen(iturl)
    itdata = web.read()
    if (cnt%3==1 and cnt>=4 and cou<=30):
        f = open('d:/pythoncode/simplecodes/image/'+str(cou)+'.png',"wb")
        cou = cou+1
        f.write(itdata)
        f.close()
        print(it)
    cnt = cnt+1
