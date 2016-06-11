# coding:utf-8
__author__ = 'zhangmengyuan'

"""
python实现任一个英文的纯文本文件，统计其中的单词出现的个数、行数、字符数
直接复制的易枭寒的代码
原文链接:http://blog.csdn.net/xiaowanggedege/article/details/9210121
"""
file_name = "./le_4/word.txt"
line_counts = 0
word_counts = 0
character_counts = 0

with open(file_name, 'r') as f:
    for line in f:
        words = line.split()

        line_counts += 1
        word_counts += len(words)
        character_counts += len(line)

print "line_counts ", line_counts
print "word_counts ", word_counts
print "character_counts ", character_counts