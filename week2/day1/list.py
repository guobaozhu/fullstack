#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  09/12/2019 7:37 PM
#  filename:  list.py
#  IDE     :  PyCharm

# index 根据内容找位置
a = ['wuchao', 'jinxin', 'ligang', 'sanpang', 'ligang', 'xiaohu']

first_index = a.index('ligang')  # 取出第一个‘ligang’的位置，然后对列表进行切片，再获得第二个‘ligang’在小列表的位置
print(first_index)
little_list = a[first_index+1:]
second_index = little_list.index('ligang')
print(second_index)
second_index_in_a = first_index + second_index + 1
print(a[second_index_in_a])


# reverse 倒叙显示列表

a = ['wuchao', 'jinxin', 'ligang', 'sanpang', 'ligang', 'xiaohu']
a.reverse()
print(a)

# sort 排序

x = [1, 5, 4, 3, 9, 6, 7]
x.sort()
x.sort(reverse=True)
print(x)


# 查某个元素在某个列表中
print(a.count('haidilao'))
print('haidilao' in a)


'''
    列表，元组
        查
            索引(下标) ，都是从0开始
            切片
            .count 查某个元素的出现次数
            .index 根据内容找其对应的位置
            "haidilao ge" in a
        增加
            a.append() 追加
            a.insert(index, "内容")
            a.extend 扩展

        修改
            a[index] = "新的值"
            a[start:end] = [a,b,c]

        删除
            remove("内容")
            pop(index)
            del a, del a[index]
            a.clear() 清空

        排序
            sort ()
            reverse()

        身份判断
            >>> type(a) is list
            True
            >>>
'''