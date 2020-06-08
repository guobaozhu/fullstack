#!/usr/bin/env python
# _*_coding:utf-8_*_

#  author  :  duke
#  date    :  18/12/2019 11:55 AM
#  filename:  menu3_plus.py
#  IDE     :  PyCharm


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

menu_layer = menu
parent_layer = []

while True:
    for key in menu_layer:
        print(key)
    choice = input('请输入>>>').strip()
    if len(choice) == 0:
        continue
    if choice in menu_layer.keys():
        print(menu_layer.keys())
        # dict_values = menu_layer.values()
        # print(dict_values[0][0])
        # if dict_values[0][0] == 0:
        #     print('已处于最底层！请输入（返回上一级：p;退出，q）：')
        parent_layer.append(menu_layer)  # 父类
        menu_layer = menu_layer[choice]  # 子类
    elif choice == 'b':
        if parent_layer:
            menu_layer = parent_layer.pop()  # 子类变父类
    elif choice == 'q':
        break
    else:
        print('无此项！')

