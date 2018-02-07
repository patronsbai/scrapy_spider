# -*- coding:utf-8 -*-

from lxml import etree
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

if __name__ == '__main__':

    html = getHtml('https://detail.1688.com/offer/528506897951.html')

    res = etree.HTML(html)
    data = res.xpath('//*[@id="mod-detail-price"]/div/table/tbody/tr[1]/td[2]/text()')
    print(data)










