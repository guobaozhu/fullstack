#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  18/12/2019 11:55 AM
#  filename:  menu3_plus.py
#  IDE     :  PyCharm
import time


def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('speed %s' % (end-start))
    return inner


@show_time  # foo=show_time(foo)
def foo():
    print('foo....')
    time.sleep(1)


@show_time
def bar():
    print('bar....')
    time.sleep(3)


foo()
bar()






