#!/usr/bin/env python
# coding=utf-8

from function.marksixdata import *
from function.common import Common

data = MarksixData()


class Collosion(object):
    '''
    碰撞算法，执行左右延长计算，此方法相对杀公式正确率和可用率更高
    '''
    # 全年正确错误数（间隔式）
    yearrighterrordrawdataarray = []
    # 全年对,错率
    yearrighterrorrate = []
    # 下期预测的数字
    nextnumberlist = []
    # 最近十期开奖结果
    lastopenresult = []
    # ===========================================
    # 正确数
    r = 0
    # 错误数
    e = 0
    # 最高连对次数
    mr = 0
    # 最高连错次数
    me = 0
    # 最新连对
    lastsetright = 0
    # 连对期数
    lastsetrightarray = []
    # 最新连错
    lastseterror = 0
    # 连错期数
    lastseterrorarray = []
    # 成本总计
    totalcost = ''
    # 预计回报
    expectedreturn = ''

    def __init__(self, outp, cost, rate, isreverse=False):
        self.outp = outp
        self.cost = cost
        self.rate = rate
        self.isreverse = isreverse
        pass

    def left_and_right_extend(self, jo, killSeq, leng=3):
        """
        预测将要开码的数字序列尾数，也不应该在大集合中执行差集操作
        :param leng: 延长长度
        :return: 没有返回
        """

        maxright = 0  # 最大正确数
        maxerror = 0  # 最大错误数
        retlist = []  # 预测数组号码
        rightarray = []  # 正确数数组
        errorarray = []  # 错误数数组
        ratarray = []  # 对错归纳数组
        temparray = []

        if leng > 4 or leng < 1:
            raise Exception("长度错误，leng小于5且大于0")

        for index in range(len(jo)):
            nextIndex = index + 1
            if nextIndex >= len(jo):
                break
            number = jo[nextIndex][1]['unusual_number']['number']
            cnumber = jo[index][1]['unusual_number']['number']
            finalarray = self.__getseqtail(cnumber, leng)
            retlist = self.__getalltail(finalarray)
            if killSeq != None:
                if len(killSeq) > 0:
                    retlist = list(set(retlist) - (set(killSeq)))

            try:
                if retlist.index(int(number)) >= 0:
                    self.r = self.r + 1
                    # 最高正确数组合
                    maxright = maxright + 1
                    self.lastsetright = self.lastsetright + 1
                    self.lastsetrightarray.append(str(index + 2).zfill(3))
                    if maxright > self.mr:
                        self.mr = maxright
                        pass
                    # 最高正确数组合

                    # 最高错误数组合
                    if maxerror > self.me:
                        self.me = maxerror
                    else:
                        maxerror = 0
                        pass
                    self.lastseterror = 0
                    self.lastseterrorarray = []
                    # 最高错误数组合
            except:
                self.e = self.e + 1
                # 最高正确数组合
                if maxright > self.mr:
                    self.mr = maxright
                else:
                    maxright = 0
                    pass
                self.lastsetright = 0
                self.lastsetrightarray = []
                # 最高正确数组合

                # 最高错误数组合
                maxerror = maxerror + 1
                self.lastseterror = self.lastseterror + 1
                self.lastseterrorarray.append(str(index + 2).zfill(3))
                if maxerror > self.me:
                    self.me = maxerror
                    pass
                # 最高错误数组合

                pass

            temparray.append(Common.e2p(retlist, number))
            if index > len(jo) - self.outp - 2:
                print(str(index + 2).zfill(3) + "期: " + \
                      "预" + str(finalarray) + "尾 " + \
                      "[" + str(len(retlist)) + "]个 " + \
                      "开[" + str(number) + "] " + \
                      Common.e2p(retlist, number))
                pass

        for index in range(len(temparray)):
            temp = {}
            nextIndex = index + 1
            if nextIndex >= len(temparray):
                # 最后一次判断
                if temparray[index] == '对':
                    rightarray.append(str(index + 2).zfill(3))
                    temp["对"] = rightarray
                    self.yearrighterrordrawdataarray.append(len(rightarray))
                    ratarray.append(temp)
                else:
                    errorarray.append(str(index + 2).zfill(3))
                    temp["错"] = errorarray
                    self.yearrighterrordrawdataarray.append(len(errorarray))
                    ratarray.append(temp)
                break

            if temparray[index] == '对':
                rightarray.append(str(index + 2).zfill(3))
                if temparray[nextIndex] == '错':
                    temp["对"] = rightarray
                    ratarray.append(temp)
                    self.yearrighterrordrawdataarray.append(len(rightarray))
                    rightarray = []
            if temparray[index] == '错':
                errorarray.append(str(index + 2).zfill(3))
                if temparray[nextIndex] == '对':
                    temp["错"] = errorarray
                    ratarray.append(temp)
                    self.yearrighterrordrawdataarray.append(len(errorarray))
                    errorarray = []

        # 设置类成员属性值
        self.nextnumberlist = retlist
        self.yearrighterrorrate.append(round((self.r / (len(jo) - 1)) * 100.0, 2))
        self.yearrighterrorrate.append(100 - self.yearrighterrorrate[0])
        self.totalcost = str(self.cost * len(retlist)) + '元(' + str(self.cost) + '/元)'
        self.expectedreturn = str((self.rate - len(retlist)) * self.cost) + '元(' + str(round(((self.rate - len(retlist)) * self.cost) / \
                                                                                             (self.cost * len(retlist)), 2)) + '倍)'

        # 输出相关的所有信息
        print('==============左右(&碰撞)预测==============')
        print('公式总计: ' + str(len(jo)) + '/' + str(len(jo) - 1))
        print('公式对错: ' + str(self.r) + '/' + str(self.e) + '/' + str(round((self.r / (len(jo) - 1)) * 100.0, 2)) + "%")
        print('最高连对: ' + str(self.mr) + '次')
        print('最新连对: ' + str(self.lastsetright) + '次')
        print('连对期数: ' + str(self.lastsetrightarray))
        print('最高连错: ' + str(self.me) + '次')
        print('最新连错: ' + str(self.lastseterror) + '次')
        print('连错期数: ' + str(self.lastseterrorarray))
        print('成本总计: ' + self.totalcost)
        print('预计回报: ' + self.expectedreturn)
        print('预测号码: ' + str(retlist) + ' 共[' + str(len(retlist)) + ']个')

    def __nextnumrightorerror(self, jocurrentnext, jonextnext, killSeq, leng):
        """
        计算判断下下期的对错
        :param jocurrentnext: 当前下期 
        :param jonextnext: 当前下下期
        :param killSeq: 其他要减去的序列
        :param leng: 尾数的左右延长数
        :return: 返回下下期判断的对错
        """
        finalarray = self.__getseqtail(jocurrentnext, leng, self.isreverse)
        retlist = self.__getalltail(finalarray)
        if killSeq != None:
            if len(killSeq) > 0:
                retlist = list(set(retlist) - (set(killSeq)))
        try:
            if retlist.index(int(jonextnext)) >= 0:
                return True
        except:
            return False

    def __getseqtail(self, cnumber, leng):
        """
        获取下一期的尾数，通过左右延长的长度来进行预测下期开奖的尾数
        核心算法
        :param cnumber: 当前号码 
        :param leng: 延长长度
        :return: 
        """
        currentnumbertail = int(str(cnumber)[1])
        if currentnumbertail == 0:
            leftarray = [9]
        else:
            currentnumbertail = int(str(cnumber)[1])
            if currentnumbertail - 1 < 0:
                currentnumbertail = 0
            leftarray = [currentnumbertail - 1]

        currentnumbertail = int(str(cnumber)[1])
        if currentnumbertail + 1 > 9:
            currentnumbertail = -1
        rightarray = [currentnumbertail + 1]

        for _ in range(leng - 1):
            lastnumber = leftarray[len(leftarray) - 1] - 1
            if lastnumber < 0:
                lastnumber = 10 + lastnumber
            leftarray.append(lastnumber)
            pass
        for _ in range(leng - 1):
            lastnumber = rightarray[len(rightarray) - 1] + 1
            if lastnumber > 9:
                lastnumber = 10 - lastnumber
            rightarray.append(lastnumber)
            pass
        leftarray.reverse()
        newarray = leftarray + [int(str(cnumber)[1])] + rightarray
        if self.isreverse:
            newarray = list(set(MarksixData.tail_data) - (set(newarray)))
        return newarray

    def __getalltail(self, finalarray):
        '''
        根据提供的数字，迭代后返回新的相关包含尾数的数字集合
        :param finalarray: 
        :return: 
        '''
        retlist = []
        for num in finalarray:
            if num == 0:
                num = 10
            for i in data.tail_number_data:
                try:
                    if i.index(num) >= 0:
                        for z in i:
                            retlist.append(z)
                except:
                    pass
        return retlist
