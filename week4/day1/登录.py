#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  18/12/2019 11:55 AM
#  filename:  menu3_plus.py
#  IDE     :  PyCharm


jdlogin_status = False
wxlogin_status = False
key = 0
def logger(auth_type):
    def login(f):
        global jdlogin_status
        global wxlogin_status
        if jdlogin_status == False:
            username = input("username:").strip()
            password = input("password:").strip()
            a = open(auth_type, 'r', encoding='utf-8')
            at = a.read()
            a.close()
            dic = eval(at)
            if username in dic and password == dic[username]:
                f()
                jdlogin_status = True
            else:
                print('账号密码错误！')
        elif wxlogin_status == False:
            username = input("username:").strip()
            password = input("password:").strip()
            a = open(auth_type, 'r', encoding='utf-8')
            at = a.read()
            a.close()
            dic = eval(at)
            if username in dic and password == dic[username]:
                f()
                wxlogin_status = True
            else:
                print('账号密码错误！')
        elif jdlogin_status == True:
            f()
        elif wxlogin_status == True:
            f()
        else:
            pass
    return login

def judge(key):
    if key == 1:
        @logger("jingdong")
        def home():
            print('welcome to home\n')
    elif key == 2:
        @logger("weixin")
        def finance():
            print('welcome to finance\n')
    else:
        @logger("jingdong")
        def book():
            print('welcome to book\n')


def start():
 global key
 list = {1: 'home', 2: 'finance', 3: 'book'}
 for i in list:
     print(i, list[i])
 select_num = input("请输入访问网页的编号[退出:q]>>")
 if select_num == 'q':
     exit()
 elif select_num.isdigit():
     select_num = int(select_num)
     if select_num in list:
        key = select_num
     else:
         print("请输入有效值！")
         return
 else:
     print("请输入有效值！")
     return
 judge(key)
while 1:
    start()
