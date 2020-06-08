#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  11/12/2019 9:38 PM
#  filename:  test.py
#  IDE     :  PyCharm


a = (1, 2, 3)  # 元祖不能修改，取一个是一个值，取多个是一个元祖
print(a[1:2])
print(a[1])
a[1] = 5  # 元祖不能修改
print(a)

