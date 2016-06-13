# coding:utf-8
__author__ = 'zhangmengyuan'

"""
一个HTML文件，找出里面的链接。
"""

from bs4 import BeautifulSoup
import urllib
import urllib2


# 要分析的网页url
url = 'http://www.ruanyifeng.com/blog/2015/05/co.html'

def find_all_link(url):
    # 获取协议，域名 proto:http rest: //www.ruanyifeng.com/blog/2015/05/co.html
    # domain:www.ruanyifeng.com
    proto, rest = urllib.splittype(url)
    domain = urllib.splithost(rest)[0]
     # 读取网页内容
    html = urllib2.urlopen(url).read()
    # 提取超链接
    a = BeautifulSoup(html).findAll('a')
     # 过滤
    alist = [i.attrs['href'] for i in a if i.attrs['href'][0] != 'j']
     # 将形如#comment-text的锚点补全成http://www.ruanyifeng.com/blog/2015/05/co.html,将形如/feed.html补全为http://www.ruanyifeng.com/feed.html
    alist = map(lambda i: proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, alist)
    return alist

link_list = find_all_link(url)
print link_list