# # -*- coding:utf-8 -*-
#
# import urllib2
# import urllib
# import time
#
#
# class Tiebaspider(object):
#
#     def __init__(self, tiebaname, star_page, end_page):
#         self.base_url = "https://tieba.baidu.com/f?"
#         self.name = tiebaname
#         self.start = star_page
#         self.end = end_page
#         self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#
#     def send_request(self, url):
#
#         time.sleep(3)
#         try:
#             request = urllib2.Request(url, headers=self.headers)
#             response = urllib2.urlopen(request)
#             if response.getcode() == 200:
#                 return response.read()
#         except Exception, err:
#             print err
#
#     def write_file(self, data, page):
#         filename = "Tieba/" + str(page) + "页.html"
#         print "%s正在下载中...." %filename
#         with open(filename, "w") as f:
#             f.write(data)
#
#     #
#     # def write_file(self, data, page):
#     #     filename = "Tieba/" + str(page) + "页.html"
#     #     print  "%s正在下载中...." % filename
#     #     with open(filename, "w") as f:
#     #         f.write(data)
#
#     def start_work(self):
#         for page in range(self.start, self.end + 1):
#             pn = (page - 1) * 50
#             params = {
#                 "kw" : self.name,
#                 "pn" : pn
#             }
#
#             params_str = urllib.urlencode(params)
#             url = self.base_url + params_str
#             data = self.send_request(url)
#             self.write_file(data, page)
#
#
# if __name__ == '__main__':
#
#     # 1.贴吧名字
#     tiebaname = raw_input("请输入贴吧名称:")
#
#     # 2.开始页
#     star_page = int(raw_input("开始页:"))
#
#     # 3.结束页
#     end_page = int(raw_input("结束页:"))
#
#     # 4. 拼接网址 发送请求
#     tool = Tiebaspider(tiebaname, star_page, end_page)
#     tool.start_work()
#
#     # 5.写入本地
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib2

import urllib

import time


class Tiebaspider(object):
    def __init__(self, tiebaname, star_page, end_page):
        self.base_url = "https://tieba.baidu.com/f?"
        self.name = tiebaname
        self.start = star_page
        self.end = end_page
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求
    def send_request(self, url):
        time.sleep(2)
        try:
            request = urllib2.Request(url, headers=self.headers)

            response = urllib2.urlopen(request)

            if response.getcode() == 200:
                return response.read()
        except Exception, err:
            print err

    def write_file(self, data, page):
        filename = "Tieba/" + str(page) + "页.html"
        print  "%s正在下载中...." % filename
        with open(filename, "w") as f:
            f.write(data)

    # 调度的方法
    def start_work(self):

        for page in range(self.start, self.end + 1):
            pn = (page - 1) * 50
            params = {
                "kw": self.name,
                "pn": pn
            }

            # url 转码
            params_str = urllib.urlencode(params)

            url = self.base_url + params_str

            # 发送请求 写入本地数据
            data = self.send_request(url)
            self.write_file(data, page)


if __name__ == '__main__':
    # 1.贴吧名字
    tiebaname = raw_input("请输入贴吧名称:")

    # 2.开始页
    star_page = int(raw_input("开始页:"))

    # 3.结束页
    end_page = int(raw_input("结束页:"))

    # 4. 拼接网址 发送请求
    tool = Tiebaspider(tiebaname, star_page, end_page)
    tool.start_work()

    # 5.写入本地

