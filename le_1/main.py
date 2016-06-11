# _*_ coding:utf-8 _*_
#写的比较粗糙 没有加错误和异常处理 图片气泡
from PIL import Image,ImageFont,ImageDraw
import os
import sys

class addPicNum:
    # 初始化图片流
    def __init__(self,filePath,fontPath):
        self.imageIO = Image.open(filePath)
        self.FontSize = min(self.imageIO.size)/8
        self.FontIO = ImageFont.truetype(fontPath,self.FontSize)
    def add_num(self):
        # draw.text (（x,y），“text,"RGB值”，字体）
        # 如果这里不-50的x坐标，那么整个“5”就处于图片的界外了，所以需要减一个数值
        # Y坐标可以设为0,这样顶部就对齐最上
        draw = ImageDraw.Draw(self.imageIO)
        draw.text((self.imageIO.size[0]-50,0),"5",(256,0,0),font = self.FontIO)
        self.imageIO.save("./le_1/output.jpg","jpeg")


# 获取当前路径
path = os.path.abspath(os.path.dirname(sys.argv[0]))
# 调用类 并初始化图片地址和字体路径
watermark = addPicNum(path+'/head.jpg',path+'/BigCaslon.ttf')
watermark.add_num()
