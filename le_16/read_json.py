# coding:utf-8
__author__ = 'zhangmengyuan'

"""
 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

"""

import json,xlwt

filepath = "./le_16/numbers.txt"

def read_json(filepath):
    datatable = xlwt.Workbook(encoding='utf-8',style_compression=0)
    newsheet = datatable.add_sheet('number',cell_overwrite_ok= True)
    with open(filepath,'r') as file_content:
        content = file_content.read()
        #转为json
        to_json = json.loads(content)

        for row,i in enumerate(to_json):
            for col,j in enumerate(i):
                newsheet.write(row,col,j)
        datatable.save('./le_16/number.xls')

read_json(filepath)