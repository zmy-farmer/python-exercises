# coding:utf-8
__author__ = 'zhangmengyuan'

"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import os
import re

def find_line(filepath):
    file_list = os.listdir(filepath)
    code,null_line,note = 0,0,0
    in_comment=False
    for file in file_list:
        try:
            name, ext = os.path.splitext(file)
            if ext==".py":
                file_content = open(filepath+"/"+file)
                line = file_content.readline()
                while line:
                    code += 1
                    if re.findall("\"\"\"$",line):
                        if in_comment:
                            in_comment = False
                        else:
                            in_comment = True
                    if not re.findall("\S",line):
                        null_line+=1
                    if line[0]=="#" or in_comment:
                        note+=1
                    line = file_content.readline()
                file_content.close()
        except:
            print "error"
    print code,null_line,note


filepath = "./le_7"
find_line(filepath)