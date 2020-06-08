#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  11/12/2019 9:51 PM
#  filename:  shopcar2.py
#  IDE     :  PyCharm


product_list = [
    ('Mac', 9000),
    ('kindle', 800),
    ('tesla', 900000),
    ('python book', 100),
    ('bike', 2000),
]
shopCar = []
flag = True

while flag:
    salary = input("请输入你的工资：")  # 输入工资
    if salary.isdigit():
        salary = int(salary)
        flag = False

        while True:
        # print(product_list)
        # for i in product_list:
        #     print(product_list.index(i), i)
            for i, v in enumerate(product_list, 1):  # 显示所有商品
                print(i, '>>>>>>', v)
            choice = input("请输入你想购买的商品序号[退出：q]：")  # 输入购买的商品序号
            if choice.isdigit():  # 判断商品序号是否为整数
                choice = int(choice)
                if 0 < choice <= len(product_list):  # 商品序号提示
                    p_item = product_list[choice-1]
                    print(p_item)
                    if p_item[1] <= salary:
                        print("你已加入 %s 到你的购物车，当前余额：%s" % (p_item[0], (salary-p_item[1])))
                        salary -= p_item[1]
                        shopCar.append(p_item)
                    else:
                        print("余额不足，%d" % (salary-p_item[1]))
                    print(p_item)
                else:
                    print("没有该商品！请输入数字(1- %d):" % len(product_list))
            elif choice == 'q':  # 输入内容是否为q，否，提示
                if shopCar:
                    print('-----------您已经购买如下商品----------')
                    # for i, v in enumerate(shopCar, 1):
                    #     print(i, '-=-=-=-', v)
                    for i in shopCar:  # 循环已购买商品
                        print(i)
                print("你的余额为：%d" % salary)
                print("欢迎下次光临！！！")
                break
            else:
                print('商品序号：必须输入数字！')
    else:
        print("你的工资：必须输入数字!")

