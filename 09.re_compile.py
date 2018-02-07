#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# import re
#
# if __name__ == '__main__':
#     # 1. 点的问题 ; DOTALL re.S
#     str = '''
#         asfdsfdsffsdb
#         ooooooooo
#         rrrrrr
#         dsfdfssB
#
#     '''
#     pattern = re.compile("a(.*)b",re.S)
#     # pattern = re.compile("a(.*)b", re.DOTALL)
#
#     # 即是re.S 又忽略大小写
#     # pattern = re.compile("a(.*)b", re.DOTALL | re.I)
#
#     result = pattern.findall(str)
#
#     print result
#
#     # 2. r"fsdsfd" 原始的字符串 -->这则
#     # \b 回退一个字节
#     # str2 = r"a\bb"
#     # print str2
#
#
#
#











#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re

if __name__ == '__main__':

    #正则 在哪里都是一样
    #每个语言 调用的方法不一致

    #re.match("\d+",str)
    # re.search("",str)
    # re.findall()


    # 1.match 默认从头开始  匹配一次
    # 纯数字的正则 ^\d+$

    match_str = "abc123"
    pattern = re.compile("\d+")

    #指点开始 和结束的位置
    result = pattern.match(match_str,3,4)

    # 2.search 默认任意位置开始 匹配一次
    result =  pattern.search(match_str,1,2)

    # 3.findall 全局 返回的是列表
    all_str = "abdsffsdbfsdsbfdsfb"
    all_pattern = re.compile(r"b")
    result = all_pattern.findall(all_str)

    # 4.finditer 全局 返回 迭代对像
    result = all_pattern.finditer(all_str)

    for page  in result:
         print page.group()

