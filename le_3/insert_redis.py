# _*_ coding:utf-8 _*_
# 需要安装redis模块 sudo pip install redis
# 操作数据库教程
import redis
import random, string

def rand_str(num, length = 7):
    rs = []
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for i in range(num):
        #所有字母和数字
        chars = string.letters +string.digits #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
        code = string.join(random.sample(chars, length)).replace(" ","")
        rs.append(code)
    r.set('code_string',rs) #存入string类型 其他的类型没搞定
    print "DONE!"
if __name__ == '__main__':
    rand_str(10)

