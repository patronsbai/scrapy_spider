# -*- coding:utf-8 -*-

import urllib
import urllib2

def search_data(keyword):

    url = "https://www.baidu.com/s?"

    params = {
        "wd":keyword
    }

    params_str = urllib.urlencode(params)
    real_url = url + params_str
    print real_url

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(real_url, headers=headers)

    response = urllib2.urlopen(request)

    return response.read()

def write_file(data):
    with open("06search.html", "w") as f:
        f.write(data)


if __name__ == '__main__':

    keyword = raw_input("请输入搜索内容")
    data = search_data(keyword)
    write_file(data)

