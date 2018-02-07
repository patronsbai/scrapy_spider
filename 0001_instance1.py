# -*- coding:utf-8 -*-
#
#
# from urllib.request import urlopen
# from urllib.request import urlretrieve
# from urllib.error import HTTPError
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# from multiprocessing.dummy import Pool as ThreadPool
# import sys,os
# import re
#
# savepath = r".\save"
#
# def mkdir(path):
#
#     if os.path.exists(path):
#         return os.mkdir(path)
#
#
# def getUrls(url):
#
#     driver= webdriver.PhantomJS()
#     html = urlopen(url)
#     bs = BeautifulSoup(html.read().decode('gbk'),"html.parser")
#     girls = bs.findAll("a",{"class":"lady-name"})
#     namewithurl = {}
#     for item in girls:
#         linkurl = item.get('href')
#         driver.get("https:"+linkurl)
#         bs1 = BeautifulSoup(driver.page_source,"html.parser")
#         links = bs1.find("div",{"class":"mm-p-info mm-p-domain-info"})
#         if links is not None:
#             links = links.li.span.get_text()
#             namewithurl[item.get_text()] = links
#             print(links)
#     return namewithurl
#
# def getImgs(parms):
#     personname = parms[0]
#     personurl = "https:"+parms[1]
#     html = urlopen(personurl)
#     bs = BeautifulSoup(html.read().decode('gbk'),"html.parser")
#     contents = bs.find("div",{"class":"mm-aixiu-content"})
#     imgs = contents.findAll("img",{"src":re.compile(r'//img\.alicdn\.com/.*\.jpg')})
#     savefilename = os.path.join(savepath,personname)
#     mkdir(savefilename)
#     print("img num :",len(imgs))
#     cnt = 0
#     for img in imgs:
#         try:
#             urlretrieve(url = "https:"+img.get("src"),filename =os.path.join(savefilename,str(cnt)+".jpg"))
#             cnt+=1
#         except HTTPError as e:
#             continue
#
# if __name__ == "__main__":
#     mkdir(savepath)
#     pagenum = 10
#     for i in range(1,pagenum):
#         urls = getUrls("https://mm.taobao.com/json/request_top_list.htm"+"?page="+str(i))
#         pool = ThreadPool(4)
#         pool.map(getImgs,urls.items())
#         pool.close()
#         pool.join()
#         # for (k,v in urls.items():
#         #     getImgs((k,v))



import re
import urllib
import urllib2
import os


def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#创建保存图片的文件夹
def mkdir(path):
  path = path.strip()
  isExists = os.path.exists(path)
  if not isExists:
    print u'新建了名字叫做',path,u'的文件夹'
    # 创建目录操作函数
    os.makedirs(path)
    return True
  else:
    # 如果目录存在则不创建，并提示目录已经存在
    print u'名为',path,u'的文件夹已经创建成功'
    return False





















