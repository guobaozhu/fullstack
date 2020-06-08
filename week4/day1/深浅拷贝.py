#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  18/12/2019 11:55 AM
#  filename:  menu3_plus.py
#  IDE     :  PyCharm

# s = [[1, 2], 'duke', 'goods']
# s1 = s.copy()
#
# # s1[1] = 'helllo'
# # print(s)
# # print(s1)
#
# s1[0][1] = 3
# print(s1)
# print(s)
import  copy

a = ['AAA', 123, [20000, 10000]]

b = a.copy()
b[0] = 'BBB'
b[1] = 345


c = copy.deepcopy(a)
print(c)
c[0] = 'CCC'
c[1] = 678
b[2][1] -= 3000
print(a)
print(b)
c[2][1] -= 5000
print(a, b, c)

