#!/usr/bin/env python
# coding=utf-8

from function.common import Common


class MathKillFixed(object):
    """
    上一期
    第一个号码的尾数不会开 （杀4个）
    第三个号码对应的生肖不会开 （杀4个）
    序列生肖不会开 （杀4个）
    平均正确率≈93.11%，    
    作者：stevelee
    版本：20171220
    """

    def __init__(self, outp=10):
        """
        初始化固定杀函数
        :param outp: 
        """
        self.outp = outp

    def fixed_kill_one_zodiac_1(self, jo):
        """
        # 根据指定的序列图杀一肖 
        :param jo:  
        :return: 
        """
        r = 0
        killnextzodiacSeq = []
        for index in range(len(jo)):
            # 根据本期特尾获取下期将要杀掉的生肖
            killnextzodiac = Common.get_next_kill_zodiac(
                str(jo[index][1]['unusual_number']['number'])[1])

            l = len(jo) - self.outp
            if index == len(jo) - 1:
                killnextzodiacSeq = Common.getnumber(killnextzodiac, 'z')
                print("=>预测杀: [" + killnextzodiac + "]")
                print("=>对应号: " + str(killnextzodiacSeq))
            nextIndex = index + 1
            if nextIndex >= len(jo):
                break

            # 下期实际生肖
            nextzodiac = jo[nextIndex][1]['unusual_number']['zodiac']

            if killnextzodiac != nextzodiac:
                r = r + 1

            if index > l - 2:
                print(str(index + 2).zfill(3) + "期: " + \
                      "杀[" + killnextzodiac + "] " + \
                      "开[" + nextzodiac + "] " + \
                      Common.e3p([killnextzodiac], nextzodiac))

        print('=>正确数: ' + str(r) + '次')
        print('=>正确率: ' + str(round((r / (len(jo) - 1)) * 100.0, 2)) + "%")
        return killnextzodiacSeq

    def fixed_kill_one_zodiac_2(self, jo):
        """
        根据指定的第三个生肖杀一肖 （94.67%）    
        :param jo: 
        :return: 
        """
        r = 0
        killnextzodiacSeq = []
        for index in range(len(jo)):

            killnextzodiac = jo[index][1]['six_number']['3']['zodiac']

            l = len(jo) - self.outp
            if index == len(jo) - 1:
                print("=>预测杀: [" + killnextzodiac + "]")
                killnextzodiacSeq = Common.getnumber(killnextzodiac, 'z')
                print("=>对应号: " + str(killnextzodiacSeq))
            nextIndex = index + 1
            if nextIndex >= len(jo):
                break

            # 下期实际生肖
            nextzodiac = jo[nextIndex][1]['unusual_number']['zodiac']

            if killnextzodiac != nextzodiac:
                r = r + 1

            if index > l - 2:
                print(str(index + 2).zfill(3) + "期: " + \
                      "杀[" + killnextzodiac + "] " + \
                      "开[" + nextzodiac + "] " + \
                      Common.e3p([killnextzodiac], nextzodiac))

        print('=>正确数: ' + str(r) + '次')
        print('=>正确率: ' + str(round((r / (len(jo) - 1)) * 100.0, 2)) + "%")
        return killnextzodiacSeq

    def fixed_kill_one_zodiac_3(self, jo):
        """
        根据指定的第五个生肖杀一肖 （94.0%）    
        :param jo: 
        :return: 
        """
        r = 0
        killnextzodiacSeq = []
        for index in range(len(jo)):

            killnextzodiac = jo[index][1]['six_number']['5']['zodiac']

            l = len(jo) - self.outp
            if index == len(jo) - 1:
                print("=>预测杀: [" + killnextzodiac + "]")
                killnextzodiacSeq = Common.getnumber(killnextzodiac, 'z')
                print("=>对应号: " + str(killnextzodiacSeq))
            nextIndex = index + 1
            if nextIndex >= len(jo):
                break

            # 下期实际生肖
            nextzodiac = jo[nextIndex][1]['unusual_number']['zodiac']

            if killnextzodiac != nextzodiac:
                r = r + 1

            if index > l - 2:
                print(str(index + 2).zfill(3) + "期: " + \
                      "杀[" + killnextzodiac + "] " + \
                      "开[" + nextzodiac + "] " + \
                      Common.e3p([killnextzodiac], nextzodiac))

        print('=>正确数: ' + str(r) + '次')
        print('=>正确率: ' + str(round((r / (len(jo) - 1)) * 100.0, 2)) + "%")
        return killnextzodiacSeq

    def fixed_kill_one_tail(self, jo):
        """
        执行杀1尾公式 （90.67%）
        :param jo:  
        :return: 
        """
        r = 0
        killnexttailSeq = ''
        for index in range(len(jo)):

            killnexttail = str(jo[index][1]['six_number']['1']['number'])[1]

            l = len(jo) - self.outp
            if index == len(jo) - 1:
                print("=>预测杀: [" + killnexttail + "]尾")
                killnexttailSeq = Common.getnumber(killnexttail, 't')
                print("=>对应号: " + str(killnexttailSeq))
            nextIndex = index + 1
            if nextIndex >= len(jo):
                break

            nexttail = str(jo[nextIndex][1]['unusual_number']['number'])[1]

            if killnexttail != nexttail:
                r = r + 1

            if index > l - 2:
                print(str(index + 2).zfill(3) + "期: " + \
                      "杀[" + killnexttail + "]尾 " + \
                      "开[" + nexttail + "] " + \
                      Common.e3p([killnexttail], nexttail))

        print('=>正确数: ' + str(r) + '次')
        print('=>正确率: ' + str(round((r / (len(jo) - 1)) * 100.0, 2)) + "%")
        return killnexttailSeq
