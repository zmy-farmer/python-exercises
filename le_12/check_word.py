# coding:utf-8
__author__ = 'zhangmengyuan'

"""
  敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
  用11的代码 改下成替换就好了
"""
filepath = './le_12/filtered_words.txt'

def filterwords(filepath):
    keyword_input = raw_input("Please input something:\n")
    try:
        file_content = open(filepath).read()
        file_array = file_content.split('\n')
        for keyword in file_array:
            if keyword in  keyword_input:
                keyword_input = keyword_input.replace(str(keyword), '*'*len(keyword))
                print keyword_input
    except:
        print "error"

filterwords(filepath)



