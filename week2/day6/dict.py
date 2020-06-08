#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  16/12/2019 5:16 PM
#  filename:  dict.py
#  IDE     :  PyCharm



'''
a = 10
b = a
print(id(a))
print(id(b))

b = 15

print(id(b))


不可变类型：整型、字符创、元组
可变类型：列表、字典


# 字典两大特点：无序、键唯一

dic1 = {'name': 'duke'}
dic2 = dict((('name', 'duke'),))
dic3 = dict([['name', 'duke'],])
'''


# # 增
# dic1 = {'name':'duke'}
# dic1['age'] = 18
# print(dic1)
#
# #setdefault键存在，不改动，返回字典中相应键的值
# ret = dic1.setdefault('age', 34)
# print(ret)
#
# #setdefault键不存在，在字典中增加新的键值对，并返回新增的键对应的值
# ret2 = dic1.setdefault('hobby', 'girl')
# print(ret2)
# print(dic1)
#
# # 转行
# print(list(dic1.keys()))
# print(list(dic1.values()))
# print(list(dic1.items()))
#
# print(dic1.items())

# string


st = 'he\tllo world {name} is {age}'

print(st.count('l'))  # 统计字符串中某个元素的个数
print(st.capitalize())  # 首字母大写
print(st.center(50, '-'))  # 居中
print(st.endswith('tty3'))  # 以某个字符串结尾
print(st.startswith('he'))  # 以某个字符串开头
print(st.expandtabs(tabsize=20))
print(st.find('w'))  # 查找到第一个元素，并将索引值返回
print(st.format(name='duke', age=27))  # 格式化输出的另一种方式
print(st.format_map({'name': 'duke', 'age': 27}))
print(st.index('w'))
print(st.isalnum())
print(st.isdecimal())  # 判断是否是一个十进制的数
print(st.isdigit())  # 是否为整型
print('3214312'.isdecimal())
print('Abc'.islower())
print('Abc'.isupper())
print('Abc'.isspace())
print('Abc'.istitle())
print('Abc'.lower())
print('Abc'.upper())
print('     Abc   \n'.strip())











