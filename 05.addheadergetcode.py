# -*- coding:utf-8 -*-

import urllib2


def load_baidu_data():

    url = "https://detail.1688.com/offer/528506897951.html"
    request = urllib2.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    request.add_header("Connection", "keep-alive")

    response = urllib2.urlopen(request)    #发送请求
    data = response.read()
    return data


def write_file(data):
    with open("051688.html", "w") as f:
        f.write(data)


if __name__ == '__main__':
    data = load_baidu_data()
    write_file(data)


