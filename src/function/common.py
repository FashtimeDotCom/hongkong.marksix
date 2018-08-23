#!/usr/bin/env python
# coding=utf-8

import json
import os
import function.marksixdata

data = function.marksixdata.MarksixData()


class Common:

    @staticmethod
    def bubble_sort(lists):
        # 大小排序（冒泡排序）
        count = len(lists)
        for i in range(0, count):
            for j in range(i + 1, count):
                if lists[i] < lists[j]:
                    lists[i], lists[j] = lists[j], lists[i]
        return lists

    @staticmethod
    def retchina(a, b):
        # 转换结果为中文
        if a == b:
            return "对"
        else:
            return "错"

    @staticmethod
    def getyeardata(y):
        # 读取文件
        fo = open(os.getcwd() + "/recods/" + str(y) + ".json", 'r+', encoding='utf8')
        c = fo.read()
        fo.close()
        return json.loads(c)

    @staticmethod
    def get(number, get="h"):
        # 取数字部分，例如头，尾，合
        if get == "h":
            return int(str(number)[0])
        elif get == "t":
            return int(str(number)[1])
        elif get == "j":
            return int(str(number)[0]) + int(str(number)[1])

    @staticmethod
    def c2e(o):
        if o == "蓝":
            return "blue"
        elif o == "红":
            return "red"
        elif o == "绿":
            return "green"

    @staticmethod
    def e3p(lists, b):
        err = False
        for l in lists:
            if l == b:
                err = True
        if err:
            return "错"
        else:
            return "对"

    @staticmethod
    def e2p(lists, b):
        try:
            if lists.index(int(b)) >= 0:
                return "对"
        except:
            return "错"

    @staticmethod
    def headavg(t):
        """
        求头数总数的平均数
        :param t: 头数总和
        :return: 除以5
        """
        return t % 5

    @staticmethod
    def tail(t):
        """
        求头数总数的平均数
        :param t: 头数总和
        :return: 除以10
        """
        return t % 10

    @staticmethod
    def get_next_kill_zodiac(o):
        """
        根据固定序列二维数组返回指定下一期的杀1肖    
        :param o: 特码尾
        :return: 根据固定序列返回指定生肖
        """
        for z in data.killzodiac:
            for zz in z:
                if zz == o:
                    return z[zz]

    @staticmethod
    def color(t):
        # 红蓝绿预测结果
        if t % 3 + 1 == 1:
            return '红'
        elif t % 3 + 1 == 2:
            return '蓝'
        elif t % 3 + 1 == 3:
            return '绿'

    @staticmethod
    def etoc(e):
        if e == "red":
            return "红"
        elif e == "blue":
            return "蓝"
        elif e == "green":
            return "绿"

    @staticmethod
    def singleordouble(t):
        # 单双预测结果
        if (t % 2 + 1) % 2 != 0:
            return '单'
        else:
            return '双'

    @staticmethod
    def nextsingleordouble(o):
        # 下期单双结果
        if int(o) % 2 == 0:
            return '双'
        else:
            return '单'

    @staticmethod
    def getnumber(o, t="h"):
        """
        获取制定类型的序列
        :param o: 头 | 尾 | 肖 | 色 | 单 五种类型的数据  
        :param t: h | t | z | c | s
        :return: 
        """
        if t == "z":
            _Common__zodiac = data.zodiacsequence()
            for z in _Common__zodiac:
                for zz in _Common__zodiac[z]:
                    if o == zz:
                        return _Common__zodiac[z][zz]['Sequence']
        elif t == "h":
            _Common_head = data.head_number_data
            for h in _Common_head:
                try:
                    if o == '0':
                        if h.index(int(1)) > -1:
                            return h
                    if h.index(int(o + '0')) > -1:
                        return h
                except:
                    pass
            pass
        elif t == "t":
            _Common_tail = data.tail_number_data
            for tt in _Common_tail:
                try:
                    if o == '0':
                        o = '1' + o
                    if tt.index(int(o)) > -1:
                        return tt
                except:
                    pass
        elif t == "c":
            if o == "红":
                return data.color_data[0]
            elif o == "蓝":
                return data.color_data[1]
            elif o == "绿":
                return data.color_data[2]
            pass
        elif t == "s":
            if o == '双':
                return data.single_or_double_data[1]
            else:
                return data.single_or_double_data[0]

    @staticmethod
    def formula_expression_hander(formulaexpression, matharray, offset=0):
        """
        对表达式进行反解析得到实际的数字
        :param formulaexpression: 表达式，比如"1t 0t 3j 5h 1o"
        :param matharray: 需要求和的数组，比如[15, 1, 17, 29, 35, 41, 11]
        :param offset: 求和偏移量，默认0
        :return: 返回[和, 反解析后的数组]，例如[56, [1, 5, 11, 4, 35]]
        """
        fexpressionarray = formulaexpression.split(' ')
        newmatharray = []
        index = 0

        for f in fexpressionarray:
            numIndex = int(f[0])
            operator = f[1]
            if operator == data.getnumbertype[0]:  # 头
                newmatharray.append(int(str(matharray[numIndex]).zfill(2)[0]))
            if operator == data.getnumbertype[1]:  # 尾
                newmatharray.append(int(str(matharray[numIndex]).zfill(2)[1]))
            if operator == data.getnumbertype[2]:  # 原
                newmatharray.append(int(matharray[numIndex]))
            if operator == data.getnumbertype[3]:  # 合 
                newmatharray.append(
                    int(str(matharray[numIndex]).zfill(2)[0]) + int(
                        str(matharray[numIndex]).zfill(2)[1]))
            if operator == data.getnumbertype[4]:  # 积 
                newmatharray.append(
                    int(str(matharray[numIndex]).zfill(2)[0]) * int(
                        str(matharray[numIndex]).zfill(2)[1]))
            index += 1
            pass
        total = 0
        for n in newmatharray:
            total += n
            pass
        total += offset
        return [total, newmatharray]


class SortNumber(object):
    def __init__(self):
        self.n01 = 0
        self.n02 = 0
        self.n03 = 0
        self.n04 = 0
        self.n05 = 0
        self.n06 = 0
        self.n07 = 0

    def sort_number(self, o, sort):
        # 获取每个号码
        sixnumber = o[1]['six_number']
        unusualnum = o[1]['unusual_number']
        # 按照掉球排序
        self.n01 = sixnumber['1']['number']
        self.n02 = sixnumber['2']['number']
        self.n03 = sixnumber['3']['number']
        self.n04 = sixnumber['4']['number']
        self.n05 = sixnumber['5']['number']
        self.n06 = sixnumber['6']['number']
        self.n07 = unusualnum['number']

        if sort == "size":
            lists = [self.n01, self.n02, self.n03, self.n04, self.n05, self.n06, self.n07]
            lists = Common.bubble_sort(lists)  # 按照大小进行排序
            self.n01 = lists[0]
            self.n02 = lists[1]
            self.n03 = lists[2]
            self.n04 = lists[3]
            self.n05 = lists[4]
            self.n06 = lists[5]
            self.n07 = lists[6]
        return [self.n01, self.n02, self.n03, self.n04, self.n05, self.n06, self.n07]
