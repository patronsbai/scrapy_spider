# !/usr/bin/env python
# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
import sys, os
import re


savepath = r".\xiaobaidian.html"

def mkdir(path):
    if os.path.exists(path):
        return os.mkdir(path)


def bs_object():
    html = """
            <html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
            <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.</p>
            <p class="story">...</p>
            <img src="https://cbu01.alicdn.com/img/ibank/2018/832/744/8276447238_1845730961.60x60.jpg" alt="INF男装|2018春夏字造系列新款街头文字玩家纯棉男式短袖T恤男"/>
            """

    # 转换类型
    soup = BeautifulSoup(html,"lxml")
    img = soup.img
    print img

if __name__ == '__main__':
    bs_object()


