# _*_ coding:utf-8 _*_
import random, string  
  
def rand_str(num, length = 7):  
    f = open('./le_2/yhm.txt','wb')
    for i in range(num):
        #所有字母和数字
        chars = string.letters +string.digits #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
        #random.choice从序列中获取一个随机元素
        #random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
        # s = [random.choice(chars) for j in range(length)]
        s = string.join(random.sample(chars, length)).replace(" ","")
        f.write(s+"\r\n")
    f.close()  
    print "DONE!"  
if __name__ == '__main__':  
    rand_str(200)

