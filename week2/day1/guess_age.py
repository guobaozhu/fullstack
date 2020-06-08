#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  10/12/2019 7:46 PM
#  filename:  guess_age.py
#  IDE     :  PyCharm

age_of_princal = 60

guess_age = int(input("请输入你的年纪>>:"))

if guess_age == age_of_princal:
    print("yes!!!")
elif guess_age > age_of_princal:
    print("try samller!!!")
else:
    print("try bigger")