#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  18/12/2019 11:55 AM
#  filename:  menu3_plus.py
#  IDE     :  PyCharm

# 集合的创建

# s = set('dukeu')
# print(s)

# sl = ['aaa', 'bbb', 'aaa']
# print(sl, type(sl))
# s2 = set(sl)
# print(s2, type(s2))


# li = [[1, 3], 2, 'duke']
# s = set(li)

# s = frozenset('dukesfa')
# print(s, type(s))
# print(2 in s)

s = set('duke')
# s.add("uu") # 添加一个元素
# print(s)

# s.update('sss')
# print(s)
# s.update([12, 'eeee'])
# print(s)

# s.remove('u')
# s.pop()

# s.clear()
# print(s)
#
# del s
# print(s)
# print(set('alex') == set('aleexl'))
# print(set('alex') < set('aleexlwww'))
# print(set('alext') and set('aleexlwww'))
# print(set('alext') or set('aleexlwww'))

a = set('12345')
b = set('45678')
print(a)
print(b)
print(a | b)  # 合集
print(a - b)  # 差集
print(b - a)  # 差集
print(a ^ b)  # 对称差集
print(a & b)  # 交集
print(a > b)  # 父集
print(b < a)  # 子集
