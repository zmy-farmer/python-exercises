# _*_ coding:utf-8 _*_
# 需要安装MySQLdb模块 安装教程 http://blog.csdn.net/little__zm/article/details/20493857
# 操作数据库教程 http://www.cnblogs.com/rollenholt/archive/2012/05/29/2524327.html
import MySQLdb
import random, string

def rand_str(num, length = 7):
    rs = []

    conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="python",charset="utf8")
    cur = conn.cursor()

    for i in range(num):
        #所有字母和数字
        chars = string.letters +string.digits #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
        code = string.join(random.sample(chars, length)).replace(" ","")
        rs.append(code)
    cur.executemany('insert into test (code) values (%s)',rs)
    conn.commit()
    cur.close()
    conn.close()
    print "DONE!"
if __name__ == '__main__':
    rand_str(10)

