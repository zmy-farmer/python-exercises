#coding:utf-8
__author__ = 'zhangmengyuan'

"""
题目:
    你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
思路:
    当前目录下遍历图片 得到图片尺寸
    iphone的分辨率是1136*640
    如果横向和纵向大于这个尺寸 则进行裁剪
"""

from PIL import Image
import os


def resize(filepath):
    file_list = os.listdir(filepath)
    for file in file_list:
        try:
            name, ext = os.path.splitext(file) #分割得到文件名和扩展名
            fileInfo = Image.open(filepath+"/"+file)
            w,h = fileInfo.size
            if w > 640:
                x = w/640.0
                w = 640
                h = int(h/x)
            if h>1136:
                x = h/1136.0
                h = 1136
                w = int(w/x)
            new_file = fileInfo.resize((w,h),Image.ANTIALIAS)
            new_file.save(filepath+"/"+name+"_thumb"+ext)
        except:
            print "error"

filepath = "./le_5"
resize(filepath)