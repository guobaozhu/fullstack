#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  10/12/2019 7:52 PM
#  filename:  print_plus.py
#  IDE     :  PyCharm


'''
理解python中print输出默认print("123")==print("123",end="\n")
print（"内容",end=""）
'''

num1 = 0

while num1 <= 5:
    print(num1, end="__")
    num2 = 0
    while num2 <= 7:
        print(num2, end="--")
        num2 += 1

    num1 += 1
    print()



'''
理解换行输出
'''


height = int(input("Height:"))
weight = int(input("Weight:"))

num_height = 1
while num_height <= height:

    num_height+=1
    num_weight = 1
    while num_weight <=weight:
        print("#",end="")
        num_weight+=1
    print()


line = 5
while line > 0:
    tmp=line
    while tmp > 0:
        print("*",end="")
        tmp-=1
    print()
    line-=1