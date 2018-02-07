#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib.request

def load_data():
    #
    # 1.URL
    url = "http://www.baidu.com"

    # 2.发送请求
    response = urllib.request.urlopen(url)

    # 3.返回数据
    data = response.read()

    print(data)

    # return data


# def write_files(data):
#     with open("02baidu.html", "w") as f:
#         f.write(data)


if __name__ == '__main__':
    load_data()



