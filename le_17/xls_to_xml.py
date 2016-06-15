# coding:utf-8
__author__ = 'zhangmengyuan'


"""
将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
安装xlrd pip install xlrd

坑
报错
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 6: ordinal not in range(128)
因为Python的str默认是ascii编码，和unicode编码冲突，所以在
f.write(xmlfile.toprettyxml(encoding = 'utf-8'))
这个地方就会报错

解决方法
加上这几句话
import sys
reload(sys)
sys.setdefaultencoding('utf8')
"""

import xlrd
import xml.dom.minidom as md
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def xls_to_xml(filepath):
    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_index(0)
    content = {}
    for i in range(sheet.nrows):
        content[i+1] = sheet.row_values(i)[1:]
    return content

def write_to_xml(path,to_path):
    # 读取xml到数组中
    xlscontent = xls_to_xml(path)
    # 创建新的xml文件
    xmlfile = md.Document()

    # 创建root节点
    root = xmlfile.createElement('root')
    # 创建students节点
    students = xmlfile.createElement('students')
    # 在xml文件中添加root节点
    xmlfile.appendChild(root)
    # 在root节点下添加students节点
    root.appendChild(students)
    #
    # # 创建备注
    comment = xmlfile.createComment('学生信息表 "id" : [名字,数学,语文,英文]')
    # 在students标签下添加comment
    students.appendChild(comment)
    #
    # # 创建文本节点
    xmlcontent = xmlfile.createTextNode(str(xlscontent))
    # # 添加文本节点到students节点下
    students.appendChild(xmlcontent)
    #
    with open(to_path, 'wb') as f:
        # 写入到文件
        f.write(xmlfile.toprettyxml(encoding = 'utf-8'))


path = "./le_17/student.xls"
to_path = "./le_17/student.xml"
write_to_xml(path,to_path)