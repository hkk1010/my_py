# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re
import requests
from phantomjs.phantom import Keys
from selenium import webdriver
import  time
import urllib

class mall():

    def __init__(self):
        self.URl="http://testmall.feiersmart.com"
        self.header={
        'Accept': 'application/python_json, text/plain, */*',
        'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0',
        'token':'IOo6ZxavD61cmaSFKJ5o3tiA4PI=',
    }

    def scrapy_img(self):
        #driver=webdriver.Chrome()
        driver = webdriver.PhantomJS()
        file = open('imgURl.txt','w')
        #driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs"))
        driver.get(self.URl)
        html=driver.page_source
        print(html)
        url_list=re.findall('src=\"(.*?)\"',html)
        img_url=[]
        for url in url_list:
           if 'm.360buyimg.com'  in  url:
               img_url.append(url)
        for i in img_url:
            file.write(i+'\n')
        file.close()

        # print("开始检查")
        # f=open("imgURL.txt",'r')
        # urllist=f.readlines()
        # for url in urllist:
        #     html = requests.head(url)
        #     code = html.status_code
        #     if code != 200 :
        #         print (url + u"访问异常")




if __name__ == '__main__':
    cla=mall()
    cla.scrapy_img()
    #cla.search_test()
