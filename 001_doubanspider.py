#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2
#
#
# class Doubanspider(object):
#
#     def __init__(self):
#         self.base_url = "https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action="
#         self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#
#     def send_request(self):
#         try:
#             request = urllib2.Request(self.base_url, self.headers)
#             response = urllib2.urlopen(request)
#             data = response.read()
#         except Exception as err:
#             print err
#
#     def write_file(self, data):
#         with open("001Doubanspider", "w") as f:
#             f.write(data)
#
# if __name__ == '__main__':
#
















import urllib2

class Doubanspider(object):
        def __init__(self):
            self.base_url = "https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action="
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
            with open("1doubanhome.html","w") as f:
                f.write(data)

        #调度的方法
        def strat_work(self):
            data = self.send_request()
            self.write_file(data)

if __name__ == '__main__':

    tool = Doubanspider()
    tool.strat_work()
    #发送请求

    #2.保存本文件