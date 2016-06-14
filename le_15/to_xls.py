# coding:utf-8
__author__ = 'zhangmengyuan'

"""
纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
"""

import re
import xlwt

filepath = "./le_15/city.txt"

def read_to_xls(filepath):
    datatable = xlwt.Workbook(encoding='utf-8',style_compression=0)
    newsheet = datatable.add_sheet('city',cell_overwrite_ok= True)
    num = 0
    with open(filepath,'r') as file_content:
        text = file_content.read()
        info = re.compile(r'"(\d+)".*?:.*?"(.*?)"')
        list = info.findall(text)
        for x in list:
            for i in range(len(x)):
                newsheet.write(num,i,x[i])
            num += 1
        datatable.save('./le_15/city.xls')

read_to_xls(filepath)