#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  09/12/2019 9:14 PM
#  filename:  shopcar.py
#  IDE     :  PyCharm


'''
购物车
salary = 5000 自己输入
1.iphone6s 5800
2.mac book 9000
3.coffee 32
4.python book 80
5.bicyle 1500
# >>>:1
    余额不足，-3000
# >>>:5
    已加入bicyle到你的购物车，当前余额：3500
# >>>:quit
    你已购买以下商品
    bicyle  1500
    coffee  30
    你的余额为：2970
    欢迎下次光临！！！
'''


goods = ['iphone X', 'Mac book', 'coffee', 'python book', 'bicyle']
goods_price = [5800, 9000, 32, 80, 1500]
flag1 = True
flag2 = True
shop_list = []


while flag1:  # 判断输入的是否为数字
    salary = input("请输入你的工资：")  # 输入工资
    if salary.isdigit():
        balance = int(salary)
        flag1 = False
    else:
        print("你的工资：必须输入数字!")

goods_list = '''
1.  iphone6s        5800元
2.  mac book        9000元
3.  coffee          32元
4.  python book     80元
5.  bicyle          1500元
'''
print(goods_list)  # 展示可购买商品

while flag2:  # 可重复选择商品

    input_goods_choice = input("请输入你想购买的商品序号：")  # 输入购买的商品序号
    if input_goods_choice.isdigit():  # 判断商品序号是否为整数
        goods_choice = int(input_goods_choice)
        if goods_choice > 5:  # 商品序号超过现有序号时，提示
            print("没有该商品！请输入数字(1-5):")
        elif balance >= goods_price[goods_choice-1]:  # 判断当前余额与购买商品价格大小
            print("你已加入 %s 到你的购物车，当前余额：%s" % (goods[goods_choice-1], (balance-goods_price[goods_choice-1])))
            balance = balance - goods_price[goods_choice-1]
            shop_list.append(goods[goods_choice-1])  # 存储已购买的商品名称
        else:
            print("余额不足，%d" % (balance-goods_price[goods_choice-1]))
            break

    elif input_goods_choice != 'quit':  # 输入内容是否为quit，否，提示
        print("商品序号：必须输入数字(1-5)！")
    else:  # 输入内容是否为quit，是，展示已购买商品
       # if shop_list:  # 输入商品序号已做限制，所以不用判断已购列表是否为空
        # print(shop_list)
        print("你已购买了以下商品：")
        length_shoplist = len(shop_list)
        # print(length_shoplist)
        item = 0
        while item < length_shoplist:  # 遍历list表格，并找出表格中对应的商品列表的位置
            # print(shop_list[item])
            # print(goods.index(shop_list[item]))
            tplt = "{0:10}\t{1:10}"
            # 取商品在goods列表中的位置，然后在goods_price中找到对应价格
            # print("%s %s元" % ((shop_list[item]), (goods_price[goods.index(shop_list[item])])))
            print(tplt.format((shop_list[item]), (goods_price[goods.index(shop_list[item])])), end='元\n')
            item += 1
        # print(goods_price[goods.index(shop_list[1])])
        print("你的余额为：%d" % balance)
        print("欢迎下次光临！！！")
        break
    # elif input_goods_choice == 'quit':
    #     break
    # else:
    #     print("商品序号：必须输入数字(1-5)！")

