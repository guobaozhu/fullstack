#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  06/12/2019 6:33 PM
#  filename:  login.py
#  IDE     :  PyCharm


"""登录接口：
1.请输入你的用户名密码
2.认证成功后现实欢迎信息
3.输错三次后锁定
"""

username = "guobaozhu"
password = "123456"
flag = True
L = []

while flag:
    input_username = input("请输入你的用户名>>>")
    input_password = input("请输入你的密码>>>")
    name_count = L.count(input_username)
    if name_count > 2:
        print("输入错误三次，账号被冻结")
        break
    # fileObject = 'class002.txt'
    # try:
    # tp = open(fileObject,'r')
    # except IOError:
    # print("文件打开失败， %s 文件不存在" % fileObject)
    # filename = tp.read()

    # while name_count >=3:
    # print("输入错误三次，账号被冻结")

    elif input_username == "":
        print("用户名不能为空！！！")

    elif (input_username == username) and (input_password == password):
        print("欢迎，" + input_username)
    else:
        print(input_username + ",密码错误！！！")
        print("请重新输入。。。")
        L.append(input_username)
        # print(L)

