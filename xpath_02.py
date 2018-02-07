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
    # res = html.xpath('//li[@class="item-inactive"]/a/@href')
    # info = data.xpath('string(.)')#实际上是去除了div中间的其他多余标签
    print(data)

# text = '''
#   <div>
#       <ul>
#            <li class="item-0"><a href="link1.html">first item</a></li>
#            <li class="item-1"><a href="link2.html">second item</a></li>
#            <li class="item-inactive"><a href="link31111.html">third item</a></li>
#            <li class="item-1"><a href="link4.html">fourth item</a></li>
#            <li class="item-0"><a href="link5.html">fifth item</a>
#        </ul>
#    </div>
#   '''




# 转成lxml格式
# selector = etree.HTML(text)
# data = selector.xpath('//li[@class="item-inactive"]/a/@href')
                     # ('//li[@class="item-inactive"]/a/@href')
# result = html_data.xpath('//li[@class="item-inactive"]/a/@href')

# info = data.xpath('string(.)')      #实际上是去除了div中间的其他多余标签
# print data
# content2=info.replace('\n','').replace(' ','')   #将换行与空格分别取代
# print(content2)

# res = etree.HTML(html)
# data = res.xpath('//div[@id="class3"]')
# info = data.xpath('string(.)')#实际上是去除了div中间的其他多余标签
# print(data)
# content2=info.replace('\n','').replace(' ','')#将换行与空格分别取代
# print(content2)








