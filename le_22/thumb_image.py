# coding:utf-8
__author__ = 'zhangmengyuan'

"""
根据手机型号缩小图片尺寸
"""


from PIL import Image
import os

size_config = {
    'iPhone5': {
        'height': 1136,
        'weight': 640
        },
    'iPhone6': {
        'height': 1334,
        'weight': 750
        },
    'iPhone6Plus': {
        'height': 2208,
        'weight': 1242
        }
}

def resize(filepath,to_filepath,phonetype='iPhone5'):
    file_list = os.listdir(filepath)
    for file in file_list:
        try:
            name, ext = os.path.splitext(file) #分割得到文件名和扩展名
            fileInfo = Image.open(filepath+"/"+file)
            w,h = fileInfo.size
            maxsize = size_config[phonetype]

            if w > maxsize['weight']:
                x = w/float(maxsize['weight'])
                w = maxsize['weight']
                h = int(h/x)
            if h > maxsize['height']:
                x = h/float(maxsize['height'])
                h = maxsize['height']
                w = int(w/x)
            new_file = fileInfo.resize((w,h),Image.ANTIALIAS)
            new_file.save(to_filepath+"/"+name+"_thumb"+ext)
        except:
            print "error"

filepath = "./le_5"
to_filepath = "./le_22"
resize(filepath,to_filepath)
