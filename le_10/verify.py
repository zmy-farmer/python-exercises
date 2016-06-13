# coding:utf-8
__author__ = 'zhangmengyuan'

"""
使用 Python 生成类似于下图中的字母验证码图片 修改
"""

from PIL import Image,ImageFont,ImageDraw,ImageFilter
import string
import random

KEY_LEN = 5
fontPath = "./le_10/BigCaslon.ttf"

def base_str():
    # return (string.letters+string.digits)
    return string.letters
def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))

#获得随机颜色
def random_color():
    return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))

def getCodePiture():
    width = 340
    height = 60
    # 创建画布
    image = Image.new('RGB', (width, height), (180,180,180))
    font = ImageFont.truetype(fontPath, 40)
    draw = ImageDraw.Draw(image)
    # 创建验证码对象
    code = key_gen()
    # 把验证码放到画布上
    for t in range(KEY_LEN):
        draw.text((60 * t + 10, 0), code[t], font=font, fill=random_color())
    # 填充噪点
    for _ in range(random.randint(1500,3000)):
        draw.point((random.randint(0,width), random.randint(0,height)), fill=random_color())
    # 模糊处理
    image = image.filter(ImageFilter.BLUR)
    # 保存名字为验证码的图片
    image.save("./le_10/" + code + '.jpg', 'jpeg');

print key_gen()
print random_color()
getCodePiture()