# -*- coding:utf-8 -*-


import urllib2
from bs4 import BeautifulSoup

class Doubanspider(object):
        def __init__(self):
            self.base_url = "https://detail.1688.com/offer/528506897951.html"
            self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        def send_request(self):
            try:
                request = urllib2.Request(self.base_url,headers=self.headers)
                response = urllib2.urlopen(request)
                if response.getcode() == 200:
                    return response.read()
            except Exception,err:
                print  err

        # 2.保存本文件
        def write_file(self,data):
            with open("xiaobaidian.html","w") as f:
                f.write(data)

        #调度的方法
        def start_work(self):
            data = self.send_request()
            self.write_file(data)

        # def parse_html(self):
        #     soup = BeautifulSoup(xiaobaidian.html, "lxml")
        #
        #     pass

if __name__ == '__main__':

    tool = Doubanspider()
    tool.start_work()





#
# 1、对这个页面发请求 url='https://detail.1688.com/offer/563841978495.html?spm=a312h.
    # 7841636.1998813769.d_pic_3.aphaBg&tracelog=p4p'
# 2、获取到页面html，用 xpath 或 bs4 对页面内容进行提取，提取出轮播图对应的所有的 div
    # （应该是<div class='tab-content-container'>这个块）块.
# 3、上一部提取的 div 块中包含了轮播图所有的图片，提取里面所有的的 ul标签下面的 li/div/a/img标签
    # 里面的 src 属性
# 4、第三部就提取到了 img 的一个集合，包含了所有的轮播图url，遍历第三部提取到的对象，
    # 对每个url地址发送请求，获取图片内容
# 5、xpath 和 bs4 怎么用看看ke件吧