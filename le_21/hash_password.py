# coding:utf-8
__author__ = 'zhangmengyuan'

"""
 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

 资料:uuid说明
 1  http://www.cnblogs.com/dkblog/archive/2011/10/10/2205200.html
 2  http://www.cnblogs.com/Security-Darren/p/4252868.html
"""

import uuid
import hashlib

def get_hash_password(password):
    # uuid 用以产生随机的盐值
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode('utf-8') + user_password.encode('utf-8')).hexdigest()

user_password = raw_input("input your password:\n")
hash_password = get_hash_password(user_password)

print "your encipher's password is:" + hash_password,"\n"

confirm_password = raw_input("please input your password for check:\n")

if check_password(hash_password,confirm_password):
    print "success"
else:
    print "something is wrong"

