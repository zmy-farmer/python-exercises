# coding:utf-8
__author__ = 'zhangmengyuan'

"""
 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
 fuck 网上都说用input("Please input something:\n")来得到用户的输出 其实是不对的 要用raw_input来得到用户输出
 好像是input得到的是python表达式 没法用in来比较
 但是raw_input得到的是string 就可以用in了
 真坑 自己都没试过的代码就好意思贴出来
"""
filepath = './le_11/filtered_words.txt'

def filterwords(filepath):
    keyword_input = raw_input("Please input something:\n")
    try:
        file_content = open(filepath).read()
        file_array = file_content.split('\n')
        for keyword in file_array:
            if keyword in  keyword_input:
                print "Freedom"
            else:
                print "Human Rights"
    except:
        print "error"

filterwords(filepath)



