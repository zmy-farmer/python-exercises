# coding:utf-8
__author__ = 'zhangmengyuan'

"""
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
安装模块(如果你没有装的话):pip install xlwt
"""


import xlwt
import re

file_path = './le_14/student.txt'
def read_to_xls(filepath):
    datatable = xlwt.Workbook(encoding='utf-8',style_compression=0)
    newsheet = datatable.add_sheet('student',cell_overwrite_ok= True)
    num = 0
    with open(filepath,'r') as file_content:
        text = file_content.read()
        info = re.compile(r'"(\d+)":\["(.*?)",(\d+),(\d+),(\d+)]')
        list = info.findall(text)
        for x in list:
            for i in range(len(x)):
                newsheet.write(num,i,x[i])
            num += 1
        datatable.save('./le_14/student.xls')

read_to_xls(file_path)