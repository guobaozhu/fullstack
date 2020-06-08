#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  06/12/2019 3:42 PM
#  filename:  code_template.py
#  IDE     :  PyCharm

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit():  # 判断输入是否为数字
    salary = int(salary)
else:
    # print("must input digit")
    exit("must input digit")  # 退出程序
msg = '''
-----------info of %s-----------
Name:%s
Age:%s
Job:%s
Salary:%s
You will be retired in %s yesrs
-----------end-------------
''' % (name, name, age, job, salary, 65-age)

print(msg)
