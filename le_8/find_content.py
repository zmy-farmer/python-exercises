# coding:utf-8
__author__ = 'zhangmengyuan'

"""
一个HTML文件，找出里面的正文
"""

import os,re

def find_body(filepath):
    try:
        file_content = open(filepath)
        line = file_content.read().decode("utf-8")
        pattern = re.compile("<body.*?>(.*?)</.*?body>",re.S)
        items = re.findall(pattern,line)
        print items[0].strip()
    except:
        print "error"


filepath = "./le_8/ceshi.html"
find_body(filepath)
