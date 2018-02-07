# -*- coding:utf-8 -*-

import urllib
from lxml import etree


# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html

if __name__ == '__main__':
    # text = getHtml("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0")

    # print text
    text = '''
      <div>
          <ul>
               <li class="item-0"><a href="link1.html">first item</a></li>
               <li class="item-1"><a href="link2.html">second item</a></li>
               <li class="item-inactive"><a href="link31111.html">third item</a></li>
               <li class="item-1"><a href="link4.html">fourth item</a></li>
               <li class="item-0"><a href="link5.html">fifth item</a>
           </ul>
       </div>
      '''
    # 1.转换成 lxml文档
    html_data = etree.HTML(text)

    # 2. 格式化
    # html_result = etree.tostring(html_data)

    # print html_result

    # # #3.4 取出 属性的值
    # < li class ="item-inactive" > < a href="link3.html" > third item < / a > < / li >
    result = html_data.xpath('//li[@class="item-inactive"]/a/@href')
    # result = html_data.xpath('//*[@id="imgid"]/div/ul/li[2]/div/a/img')
    print result
    # # #3.5 模糊查询 contains
    # result1 = html_data.xpath('//li[contains(@class,"1")]')
    #
    # print result1


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
