#!/usr/bin/env python
# coding=utf,8

import numpy as np
import copy


class MarksixData(object):
    # 公式取数方式
    getnumbertype = ['h', 't', 'o', 'j', 'a']

    # 用于基础计算中的全局变量
    currnetmarksix = [0, 0, 0, 0, 0, 0, 0]

    # 尾数合集(0-9)
    tail_data = np.arange(0, 10, 1)

    # 五行生肖（固定）
    five_lines = {
        '金': {'Sequence': ['猴', '鸡']},
        '木': {'Sequence': ['虎', '兔']},
        '水': {'Sequence': ['鼠', '猪']},
        '火': {'Sequence': ['蛇', '马']},
        '土': {'Sequence': ['牛', '龙', '羊', '狗']}
    }
    # 五行相克（固定）
    five_lines_mutex = [
        ['金', '木'],
        ['土', '水'],
        ['火', '金'],
        ['木', '土'],
        ['水', '火']
    ]

    # 十二生肖集合（固定）
    zodiacs = ['鼠', '牛', '虎', '兔',
               '龙', '蛇', '马', '羊',
               '猴', '鸡', '狗', '猪']

    # 反十二生肖集合（固定）
    r_zodiac = ['猪', '狗', '鸡', '猴',
                '羊', '马', '蛇', '龙',
                '兔', '虎', '牛', '鼠']

    # 49个数字集合（固定）
    number_data = np.arange(1, 50).tolist()

    # 波色集合（固定）
    color_data = [
        # 红
        [1, 2, 7, 8, 12, 13, 18, 19, 23, 24, 29, 30, 34, 35, 40, 45, 46],
        # 蓝
        [3, 4, 9, 10, 14, 15, 20, 25, 26, 31, 36, 37, 41, 42, 47, 48],
        # 绿
        [5, 6, 11, 16, 17, 21, 22, 27, 28, 32, 33, 38, 39, 43, 44, 49]
    ]

    # 大数集合（固定）
    large_data = np.arange(25, 49).tolist()

    # 小数集合（固定）
    small_data = np.arange(1, 24).tolist()

    # 合数集合（固定）
    join_data_01 = [1, 10]
    join_data_02 = [2, 11, 20]
    join_data_03 = [3, 12, 21, 30]
    join_data_04 = [4, 13, 22, 31, 40]
    join_data_05 = [5, 14, 23, 32, 41]
    join_data_06 = [6, 15, 24, 33, 42]
    join_data_07 = [7, 16, 25, 34, 43]
    join_data_08 = [8, 17, 26, 35, 44]
    join_data_09 = [9, 18, 27, 36, 45]
    join_data_10 = [19, 28, 37, 46]
    join_data_11 = [29, 38, 47]
    join_data_12 = [39, 48]
    join_data_13 = [49]

    # 合大（固定）
    join_large_data = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 30, 31, 32, 33,
                       40, 41, 42]

    # 合小（固定）
    join_small_data = [7, 8, 9, 16, 17, 18, 19, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 43, 44,
                       45, 46, 47, 48, 49]

    # 头数集合（固定）
    head_number_data = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
        [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
    ]

    # 尾数集合（固定）
    tail_number_data = [
        [10, 20, 30, 40],
        [1, 11, 21, 31, 41],
        [2, 12, 22, 32, 42],
        [3, 13, 23, 33, 43],
        [4, 14, 24, 34, 44],
        [5, 15, 25, 35, 45],
        [6, 16, 26, 36, 46],
        [7, 17, 27, 37, 47],
        [8, 18, 28, 38, 48],
        [9, 19, 29, 39, 49]
    ]

    # 单双集合（固定）
    single_or_double_data = [
        # 单数
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47,
         49],
        # 双数
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
    ]

    # 尾大（固定）
    tail_large_data = [5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 25, 26, 27, 28, 29, 35, 36, 37, 38, 39,
                       45, 46, 47, 48, 49]

    # 尾小（固定）
    tail_small_data = [1, 2, 3, 4, 10, 11, 12, 13, 14, 20, 21, 22, 23, 24, 30, 31, 32, 33, 34, 40,
                       41, 42, 43, 44]

    # 门数集合（集合）
    door_number_data_00 = np.arange(1, 9).tolist()
    door_number_data_01 = np.arange(10, 18).tolist()
    door_number_data_02 = np.arange(19, 27).tolist()
    door_number_data_03 = np.arange(28, 37).tolist()
    door_number_data_04 = np.arange(38, 49).tolist()

    # 半波集合（固定）
    half_red_even = [2, 8, 12, 18, 24, 30, 34, 40, 46]
    half_red_bill = [1, 7, 13, 19, 23, 29, 35, 45]
    half_blue_even = [4, 10, 14, 20, 26, 36, 42, 48]
    half_blue_bill = [3, 9, 15, 25, 31, 37, 41, 47]
    half_green_even = [6, 16, 22, 28, 32, 38, 44]
    half_green_bill = [5, 11, 17, 21, 27, 33, 39, 43, 49]

    # 半单双（固定）
    small_bill = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    small_even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    large_bill = [25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
    large_even = [26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

    # 段位集合（固定）
    dondata01 = np.arange(1, 7).tolist()
    dondata02 = np.arange(8, 14).tolist()
    dondata03 = np.arange(15, 21).tolist()
    dondata04 = np.arange(22, 28).tolist()
    dondata05 = np.arange(29, 35).tolist()
    dondata06 = np.arange(36, 42).tolist()
    dondata07 = np.arange(43, 49).tolist()

    # 尾数杀肖（固定）
    killzodiac = [
        {"0": "猪"},
        {"1": "狗"},
        {"2": "鸡"},
        {"3": "蛇"},
        {"4": "猪"},
        {"5": "猪"},
        {"6": "兔"},
        {"7": "马"},
        {"8": "鸡"},
        {"9": "牛"}
    ]

    def __init__(self, zodiacname='鸡'):
        self.zodiac = zodiacname

    def zodiacsequence(self):
        """
        十二生肖对应的不同号码集合
        :return: 
        """
        i = 0
        reversalZodiac = copy.deepcopy(self.r_zodiac)
        split = 0
        b = {}
        for z in self.zodiacs:
            if z == self.zodiac:
                split = i
            i = i + 1
        befor = (len(self.zodiacs) - split)
        i = 0
        for z in reversalZodiac:
            if i != befor:
                b[i] = z
            if i == befor:
                break
            i = i + 1
        for _ in b:
            del reversalZodiac[0]
        fast = b[len(b) - 1]
        del b[len(b) - 1]
        retZodiac = [fast]
        for z in reversalZodiac:
            retZodiac.append(z)
        for bb in b:
            retZodiac.append(b[bb])
        return {
            1: {retZodiac[0]:
                    {'Sequence': [1, 13, 25, 37, 49],
                     'Color': ['red', 'red', 'blue', 'blue', 'green']}},
            2: {retZodiac[1]:
                    {'Sequence': [2, 14, 26, 38], 'Color': ['red', 'blue', 'blue', 'green']}},
            3: {retZodiac[2]:
                    {'Sequence': [3, 15, 27, 39], 'Color': ['blue', 'blue', 'green', 'green']}},
            4: {retZodiac[3]:
                    {'Sequence': [4, 16, 28, 40], 'Color': ['blue', 'green', 'green', 'red']}},
            5: {retZodiac[4]:
                    {'Sequence': [5, 17, 29, 41], 'Color': ['green', 'green', 'red', 'blue']}},
            6: {retZodiac[5]:
                    {'Sequence': [6, 18, 30, 42], 'Color': ['green', 'red', 'red', 'blue']}},
            7: {retZodiac[6]:
                    {'Sequence': [7, 19, 31, 43], 'Color': ['red', 'red', 'blue', 'green']}},
            8: {retZodiac[7]:
                    {'Sequence': [8, 20, 32, 44], 'Color': ['red', 'blue', 'green', 'green']}},
            9: {retZodiac[8]:
                    {'Sequence': [9, 21, 33, 45], 'Color': ['blue', 'green', 'green', 'red']}},
            10: {retZodiac[9]:
                     {'Sequence': [10, 22, 34, 46], 'Color': ['blue', 'green', 'red', 'red']}},
            11: {retZodiac[10]:
                     {'Sequence': [11, 23, 35, 47], 'Color': ['green', 'red', 'red', 'blue']}},
            12: {retZodiac[11]:
                     {'Sequence': [12, 24, 36, 48], 'Color': ['red', 'red', 'blue', 'blue']}},
        }
