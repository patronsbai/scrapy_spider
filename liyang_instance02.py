#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from  lxml import etree
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

if __name__ == '__main__':

    text = getHtml("https://detail.1688.com/offer/530749603338.html")

    # 1.转换成 lxml文档
    html_data = etree.HTML(text)

    # 2. 格式化 了解
    html_result = etree.tostring(html_data)
    # print  html_result
    #3.掌握的 xpath
    #3.1取出所有的li标签
    # result = html_data.xpath('//li')
    #3.2获取所有a
    # result = html_data.xpath('//li/a')
    #
    # #3.3 取出内容
    # result = html_data.xpath('//li/a/text()')
    #
    #3.4 取出 属性的值
    result = html_data.xpath('//*[@id="mod-detail-price"]/div/table/tbody/tr[1]/td[2]/span[2]')
    print result
    # #3.5 模糊查询 contains
    # result1 = html_data.xpath('//li[contains(@class,"1")]')
    #
    # print result1