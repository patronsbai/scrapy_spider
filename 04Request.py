# -*- coding:utf-8 -*-

import urllib2

def load_baidu_data():

    URL = "http://www.baidu.com"
    request = urllib2.Request(URL)       #构建请求对象
    response = urllib2.urlopen(request)  #发送请求
    
    data = response.read()
    return data


def write_data(data):

    with open("04baidu.html", "w") as f:
        f.write(data)

if __name__ == '__main__':
    data = load_baidu_data()
    write_data(data)












