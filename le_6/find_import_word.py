# -*- coding: utf-8 -*-
__author__ = 'zhangmengyuan'

"""
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
写的乱七八糟的 review的时候在完善
"""
import os
import re

def find_word(filepath):
    file_list = os.listdir(filepath)
    for file in file_list:
        keywords = {}
        try:
            name, ext = os.path.splitext(file) #分割得到文件名和扩展名
            if ext==".txt":
                file_content = open(filepath+"/"+file)
                line = file_content.readline()
                while line:
                    word_list = re.findall(r'[a-zA-Z]+', line.lower())
                    for word in word_list:
                        if word in keywords:
                            keywords[word] += 1
                        else:
                            keywords[word] = 1
                    line = file_content.readline()
                file_content.close()
                #用lambda表达式来排序，更灵活
                results = sorted(keywords.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
                print(u"in the %s file，%s is keyword，count is %s times" % (name, results[0][0], results[0][1]))
        except:
            print "error"



filepath = "./le_6"
find_word(filepath)


