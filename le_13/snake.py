# coding:utf-8
__author__ = 'zhangmengyuan'

"""
用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
"""

import urllib
import urllib2
import re
import os


def get_content(url):
    try:
        # 构建请求的request
        request = urllib2.Request(url)
        # 利用urlopen获取页面代码
        response = urllib2.urlopen(request)
        # 将页面转换为utf8编码
        pageCode = response.read().decode("utf-8")
        return pageCode
    except urllib2.URLError,e:
        if hasattr(e,'reason'):
            print u"连接失败 失败原因" + e.reason
            return None

def snake(url):
    pageCode = get_content(url)
    if not pageCode:
        print "页面加载失败..."
        return None

    pattern = re.compile('<img.*?pic_type="0".*?class="BDE_Image".*?src="(.*?)"',re.S)
    items = re.findall(pattern,pageCode)
    #用来存储图片数组
    pageStories = []
    #遍历正则表单时匹配到的信息
    for item in items:
        filename =  os.path.basename(item)
        urllib.urlretrieve(item, "./le_13/"+filename)
        print("success!" + filename)
    return pageStories


url = 'http://tieba.baidu.com/p/2166231880'
snake(url)
