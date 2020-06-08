#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  10/12/2019 7:44 PM
#  filename:  list99.py
#  IDE     :  PyCharm

'''
输出99乘法表
'''


#####1#####

print("\n")
print("开始输出99乘法表。。。")
print("\n", end="")
for a in range(1, 10):
    for b in range(1, a + 1):
        print("%dX%d=%2s" % (b, a, a * b), end="  ")
        # print("\n")
    print("\n", end="")
print("\n""end !!!")


######2####
first = 1
while first <= 9:
    second = 1
    while second <= first:
        print(str(second)+"*"+str(first)+"=", first*second, end="\t")
        second += 1
    first += 1
    print()

