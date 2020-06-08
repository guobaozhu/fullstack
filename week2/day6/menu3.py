#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  17/12/2019 11:17 AM
#  filename:  menu3.py
#  IDE     :  PyCharm


'''
1.打印省市县三级菜单
2.可返回上一级
3.可随时退出程序
'''


menu = {
    '北京': {
        '朝阳': {
            '国贸': {
                'CICC': {},
                'HP': {},
                'CCTV': {},
            },
            '望京': {
                '陌陌': {},
                '奔驰': {},
                '360': {},
            },
            '三里屯': {
            '优衣库': {},
            'Apple': {},
            },
        },
        '海淀': {
            '五道口': {
                '谷歌': {},
                '网易': {},
                'Sohu': {},
                'SOGO': {},
                '抖音': {},
                      },
            '中关村': {
                '优酷': {},
                'Iqiyi': {},
                '汽车之家': {},
                '新东方': {},
                'QQ': {},
                       },
                },
        '房山': {
            '长阳': {
                '长阳半岛': {},
                '长阳公园': {},
                '长阳CBD': {},
                    },
            '良乡': {
                '房山天街': {},
                '房山铁瓷': {},
                '新镇': {},
                    },
            '房山城区': {
                '窦店': {},
            },
        },
    },
    '上海': {
        '浦东': {
            '陆家嘴': {
                    'CICC': {},
                    '高盛': {},
                    '摩根': {},
            },
            '浦东软件园': {},
            '外滩': {},
        },
        '静安': {},
        '宝山': {},
    },
    '河南': {
        '郑州': {
            '二七广场': {},
            '郑州大学': {},
            '华北水利水电大学': {},
        },
        '驻马店': {
            '遂平县': {},
            '平舆县': {},
            '西平县': {},
        },
        '商丘': {
            '梁园区': {},
        },
    }
}
exit_flag = False

while not exit_flag:
    for key in menu:
        print(key)
    choice = input('请输入你想查看的省份：').strip()
    if choice in menu.keys():  # 判断省份是否在字典中

        while not exit_flag:
            for key2 in menu[choice]:
                print(key2)
            # 选择对应的市
            choice2 = input('请输入你想查看的市：')
            if choice2 in (menu[choice]).keys():

                # 选择对应的镇或区
                while not exit_flag:
                    for key3 in menu[choice][choice2]:
                        print(key3)
                    # 选择对应的镇或区
                    choice3 = input('请输入你想查看的镇或区：')
                    if choice3 in (menu[choice][choice2]).keys():

                        while not exit_flag:
                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)
                            print('end!!!')
                            # 选择对应的镇或区
                            choice4 = input('请输入（返回上一级：p;退出，q）：')
                            # if choice4 in (menu[choice][choice2][choice3]).keys():

                            if choice4 == 'q':
                                exit_flag = True
                                print('over!!!')
                            elif choice4 == 'p':
                                break
                            else:  # 输入不正确信息，展示现有可选择
                                print('请输入列表中的镇或区！列表如下：')

                    elif choice3 == 'q':
                        exit_flag = True
                        print('over!!!')
                    elif choice3 == 'p':
                        break
                    else:  # 输入不正确信息，展示现有可选择
                        print('请输入列表中的镇或区！列表如下：')

            elif choice2 == 'q':
                exit_flag = True
                print('over!!!')
            elif choice2 == 'p':
                break
            else:  # 输入不正确信息，展示现有可选择
                print('请输入列表中的市！列表如下：')

    elif choice == 'q':
        exit_flag = True
        print('over!!!')
    else:  # 输入不正确信息
        print('请输入列表中的省份！列表如下：')


