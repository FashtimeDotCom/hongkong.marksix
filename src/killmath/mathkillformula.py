#!/usr/bin/env python
# coding=utf-8


from function.common import Common
from function.common import SortNumber
import function.formula as fr
from function.marksixdata import *

data = MarksixData()

'''
根据公式进行杀头杀尾操作
作者：stevelee
版本：20171227
'''


class MathKillFormula(object):

    def __init__(self, oup=10):
        self.outp = oup
        self.sortnumber = SortNumber()

    def kill_head_formula(self, jo, sort):
        """
        执行杀1头公式 （90.0%）
        :param jo: 年集合
        :param sort: 排序方式 默认根据落球顺序进行排序
        :return: 返回最新一期杀头数字
        """
        r = 0
        killnextheadseq = []
        for index in range(len(jo)):

            sn = self.sortnumber.sort_number(jo[index], sort)
            killnexthead = str(Common.headavg(fr.funhed(sn)))

            l = len(jo) - self.outp
            if index == len(jo) - 1:
                print("=>预测杀: [" + killnexthead + "]头")
                killnextheadseq = Common.getnumber(killnexthead, 'h')
                print("=>对应号: " + str(killnextheadseq))
            nextIndex = index + 1
            if nextIndex >= len(jo):
                break

            nextnumber = jo[nextIndex][1]['unusual_number']['number']  # 下期特码
            nexthead = str(nextnumber).zfill(2)[0]  # 下期特码头

            if killnexthead != nexthead:
                r = r + 1

            if index > l - 2:
                print(str(index + 2).zfill(3) + "期: " + \
                      "杀[" + killnexthead + "]头 " + \
                      "开[" + nextnumber + "] " + \
                      Common.e3p([killnexthead], nexthead))

        print('=>正确数: ' + str(r) + '次')
        print('=>正确率: ' + str(round((r / (len(jo) - 1)) * 100.0, 2)) + "%")
        return killnextheadseq

    def kill_tail_formula(self, jo):
        """
        执行杀1尾公式
        :param jo: 年集合
        :param sort: 排序方式 默认根据落球顺序进行排序
        :return: 返回最新一期杀头数字
        """
        r = 0
        killnexttailseq = []
        nextIndex = 0
        for index in range(len(jo)):

            killnexttailseq = fr.formulakilltail(jo[index])

            l = len(jo) - self.outp
            if index == len(jo) - 1:
                print("=>对应号: " + str(killnexttailseq))
            nextIndex += 1
            if nextIndex >= len(jo):
                break

            nextnumber = int(jo[nextIndex][1]['unusual_number']['number'])  # 下期特码

            try:
                if list(set(data.number_data) - (set(killnexttailseq))).index(nextnumber) >= 0:
                    r += 1
            except:
                pass

            if index > l - 2:
                print(str(index + 2).zfill(3) + "期: " + \
                      "杀" + str(killnexttailseq) + \
                      " 开[" + str(nextnumber).zfill(2) + "] " + \
                      Common.e3p(killnexttailseq, nextnumber))
        print('=>总数: ' + str((len(jo) - 1)))
        print('=>正确数: ' + str(r) + '次')
        print('=>正确率: ' + str(round((r / (len(jo) - 1)) * 100.0, 3)) + "%")
        return killnexttailseq

    def kill_color_bo_formula(self, jo, sort):
        """
        杀波色 （75.0%）
        :param jo: 
        :param sort: 
        :return: 
        """
        r = 0
        killcolorboseq = []
        for index in range(len(jo)):
            swq = data.number_data
            sn = self.sortnumber.sort_number(jo[index], sort)

            killcolorbo = Common.color(fr.funclr(sn))
            killcolorboseq = Common.getnumber(killcolorbo, 'c')

            l = len(jo) - self.outp
            if index == len(jo) - 1:
                print("=>预测杀: [" + killcolorbo + "]")
                print("=>对应号: " + str(killcolorboseq))
            nextIndex = index + 1
            if nextIndex >= len(jo):
                break
                pass

            nextnumber = jo[nextIndex][1]['unusual_number']['number']  # 下期特码
            nextcolor = Common.etoc(jo[nextIndex][1]['unusual_number']['color'])  # 特码波色
            swq = list(set(swq) - (set(killcolorboseq)))

            try:
                if swq.index(int(nextnumber)) >= 0:
                    r = r + 1
            except:
                pass

            # if killcolorbo != nextcolor:
            #     r = r + 1

            if index > l - 2:
                print(str(index + 2).zfill(3) + "期: " + \
                      "杀[" + killcolorbo + "] " + \
                      "开[" + nextcolor + "] " + \
                      Common.e3p([killcolorbo], nextcolor))

        print('=>正确数: ' + str(r) + '次')
        print('=>正确率: ' + str(round((r / (len(jo) - 1)) * 100.0, 2)) + "%")
        return killcolorboseq

    def kill_single_or_double(self, jo, sort):
        """
        杀单双 （62%）
        :param jo: 
        :param sort: 推荐按照落球顺序 nosize
        :return: 
        """
        r = 0
        killsingledoubleseq = []
        for index in range(len(jo)):

            sn = self.sortnumber.sort_number(jo[index], sort)
            killsingledouble = Common.singleordouble(fr.funeob(sn))

            l = len(jo) - self.outp
            if index == len(jo) - 1:
                killsingledoubleseq = Common.getnumber(killsingledouble, 's')
                print("=>预测杀 [" + killsingledouble + "]")
                print("=>对应号: " + str(killsingledoubleseq))
            nextIndex = index + 1
            if nextIndex >= len(jo):
                break

            nextnumber = jo[nextIndex][1]['unusual_number']['number']  # 下期特码
            nextsgledu = Common.nextsingleordouble(nextnumber)

            if killsingledouble != nextsgledu:
                r = r + 1

            if index > l - 2:
                print(str(index + 2).zfill(3) + "期: " + \
                      "杀[" + killsingledouble + "] " + \
                      "开[" + nextsgledu + "] " + \
                      Common.e3p([killsingledouble], nextsgledu))

        print('=>正确数: ' + str(r) + '次')
        print('=>正确率: ' + str(round((r / (len(jo) - 1)) * 100.0, 2)) + "%")
        return killsingledoubleseq
