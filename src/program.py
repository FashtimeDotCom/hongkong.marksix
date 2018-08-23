#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-   

from killmath.mathkillfixed import *
from killmath.mathkillformula import *
from collisionmath.leftandright import *
from function.common import *
from function.marksixdata import *
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

"""
===============================> 六合彩左右式算法计算器说明 <===============================
=》号码左延长和右延长
=》尾数左延长和右延长
===============================> 六合彩公式杀算法计算器说明 <===============================
=》执行条件公式越多，错误率越大，得到的号码越少，预期收益越高。
=》反之条件公式越少，正确率越高，得到的号码越多，预期收益更低。
=》最多号码可达49个，最少号码可减少到只剩余2~4个
=》全年总共开奖次数和公式计算次数不相等，公式计算比全年次数少1期，这一期做基准数据
-----------------------------------------------------------------------------------------

[保守买法]：
只选择大于或等于94%正确率的条件公式进行杀码，最终会生成数字集合较多的序列，按照目前最大正确率94.6%，需
要购买高达45个号码，每个号码下注10元，不中亏450，中则净赚30。
唯一坏处是购买号码较多，且仍有6%的几率不会中奖！
[大胆买法]：
所有公式运行一遍，最终会生成2~4个号码，假如取中间数字为3个号码，每个号码下注10元，不中亏30，中净赚450。
唯一坏处是几率较小，按照全年公式150期，只中了46期，命中率为30.6%！
[平衡买法]：
在保守买法中，每个号码将注本由10元下降为5元，44个号码总计成本为220元。再加上大胆买法中的三个号码，每个
保留10元总计成本30元。两种买法成本相加和为250，结果：
有6%的几率输掉所有成本，但总成本只为250元
有94%的几率赢回5元的注本，但结果仍然只是亏掉10元
但是，一旦命中30%的注本，那么将净赚480-250=230元

只想赢，而博彩不一定都会赢，按照上面的平衡买法，相对输钱几率虽然不大，赚得也不多，但基本不会赔本，纯玩！
-----------------------------------------------------------------------------------------

目前最高单个公式正确率尾94.67%，还需要再提高，最好能达到98%以上(最多错三次)，否则合并条件后会死掉更多
=========================================================================================
"""
# 固定数据
__beginyear                     = 2018      # 计算开始年份       
__endyear                       = 2018      # 计算结束年份
__outnumber                     = 200       # 条件公式输出数
__rate                          = 48        # 赔率
__cost                          = 5         # 单个号码注本/元
__isexetotalrightrate           = 0         # 执行全年正确率并输入最新一期的开奖号码
pass
# 公式杀号
__isformulakillsingledouble     = 0         # 是否执行杀单双公式 (62.0%)
__isformulakillcolor1           = 0         # 是否执行杀波色公式 (75.0%)
__isformulakilltail1            = 0         # 是否执行杀一尾公式 (94.0%) 
__isformulakillhead1            = 0         # 是否执行杀一头公式 (90.0%)
__formulakillcolorsort          = "size"    # 对号码颜色进行排序
__formulakillheadsort           = "size"    # 对号码头进行排序
__formulakilltailsort           = "nosize"  # 对号码尾进行排序
__formulakillsingledoublesort   = "nosize"  # 对号码单双进行排序
pass
# 固定杀号
__isfixedkilltaill1             = 0         # 是否执行杀一尾公式 (90.6%)
__isfixedkillzodiac1            = 0         # 是否执行杀一肖公式 (94.6%)
__isfixedkillzodiac2            = 0         # 是否执行杀一肖公式 (94.6%)
__isfixedkillzodiac3            = 0         # 是否执行杀一肖公式 (94.0%)
pass
# 预测号码
__isleftright                   = 1         # 是否执行左右延长计算
__collisionlength               = 3         # 左右延长长度 （例如3，加上本身开码的数字，一共是7个尾数）
__isexeckillnumber              = 0         # 是否执行消公式
__isreverseleftright            = 1         # 是否取反左右延长长度（例如延长长度为3，那么取反得到是剩下的3个尾数）
pass
__isdrawimage                   = 0         # 图例绘制

# 实例化各个类，并初始化变化
common = Common()
Sortnumber = SortNumber()
collosion = Collosion(__outnumber, __cost, __rate, __isreverseleftright)
mathkillfixed = MathKillFixed(__outnumber)
mathkillformula = MathKillFormula(__outnumber)
data = function.marksixdata.MarksixData()

mpl.rcParams['font.sans-serif'] = ['simsun'] #指定默认字体为中文幼圆
mpl.rcParams['axes.unicode_minus'] = False

def main():
    global killcolor, killtail1, killhead, killzodiac1, killzodiac2, killzodiac3, killtail2, killsingleordouble, killseq
    killseq = []
    if __isfixedkillzodiac3:
        killzodiac3 = mathkillfixed.fixed_kill_one_zodiac_3(coldata())
        killseq = killzodiac3 
    if __isfixedkillzodiac2:
        killzodiac2 = mathkillfixed.fixed_kill_one_zodiac_2(coldata())
        killseq = killzodiac2
    if __isfixedkillzodiac1:
        killzodiac1 = mathkillfixed.fixed_kill_one_zodiac_1(coldata())
        killseq = killzodiac1
    if __isfixedkilltaill1:
        killtail1 = mathkillfixed.fixed_kill_one_tail(coldata())
        killseq = killtail1
    if __isformulakilltail1:
        killtail2 = mathkillformula.kill_tail_formula(coldata())
        killseq = killtail2
    if __isformulakillhead1:
        killhead = mathkillformula.kill_head_formula(coldata(), __formulakillheadsort)
        killseq = killhead
    if __isformulakillcolor1:
        killcolor = mathkillformula.kill_color_bo_formula(coldata(), __formulakillcolorsort)
        killseq = killcolor
    if __isformulakillsingledouble:
        killsingleordouble = mathkillformula.kill_single_or_double(coldata(),__formulakillsingledoublesort)
        killseq = killsingleordouble
    if __isexetotalrightrate:
        r = mathtotalrightrate(coldata())
        mathcurrentexclude(r)
        pass
    if __isleftright:
        if __isexeckillnumber:
            collosion.left_and_right_extend(coldata(), killseq, __collisionlength)
        else:
            collosion.left_and_right_extend(coldata(), [], __collisionlength)
    if __isdrawimage:
        drawimage()
    

def coldata():
    year = np.arange(__beginyear, __endyear + 1).tolist()
    yt = common.getyeardata(year[0])
    for y in range(len(year)):
        y = y + 1
        if y == len(year):
            break
        yt = list(yt + common.getyeardata(year[y]))
    return yt


# 预测本期所开的所有号码
def mathcurrentexclude(r):
    swq = data.number_data
    if __isfixedkillzodiac2:
        swq = list(set(swq) - (set(killzodiac2)))
    if __isfixedkillzodiac1:
        swq = list(set(swq) - (set(killzodiac1)))
    if __isfixedkillzodiac3:
        swq = list(set(swq) - (set(killzodiac3)))
    if __isfixedkilltaill1:
        swq = list(set(swq) - (set(killtail1)))
    if __isformulakilltail1:
        swq = list(set(swq) - (set(killtail2)))
    if __isformulakillhead1:
        swq = list(set(swq) - (set(killhead)))
    if __isformulakillcolor1:
        swq = list(set(swq) - (set(killcolor)))
    if __isformulakillsingledouble:
        swq = list(set(swq) - (set(killsingleordouble)))
        pass
    print('预测号码: ' + str(swq) + ' 共[' + str(len(swq)) + ']个')
    print('成本总计: ' + str(__cost * len(swq)) + '(' + str(__cost) + '/元)')
    print('预计回报: ' + str((__rate - len(swq)) * __cost) + '元(' + str(
        round(((__rate - len(swq)) * __cost) / (__cost * len(swq)), 2)) + '倍)')
    pass


# 统计本年集合中所有需要预测号码的准确率
def mathtotalrightrate(jo):
    r = 0
    e = 0
    mr = 0
    maxright = 0
    lastsetright = 0
    lastsetrightarray = []
    for index in range(len(jo)):
        swq = data.number_data

        nextIndex = index + 1
        if nextIndex >= len(jo):
            break
        nextnumber = int(jo[nextIndex][1]['unusual_number']['number'])
        pass
        # 杀1肖 
        killnextzodiac = Common.get_next_kill_zodiac(
            str(jo[index][1]['unusual_number']['number'])[1])
        killnextzodiacseq = Common.getnumber(killnextzodiac, 'z')
        if __isfixedkillzodiac1:
            swq = list(set(swq) - (set(killnextzodiacseq)))
            pass
        # 杀1肖
        killnextzodiac = jo[index][1]['six_number']['3']['zodiac']
        killnextzodiacseq = Common.getnumber(killnextzodiac, 'z')
        if __isfixedkillzodiac2:
            swq = list(set(swq) - (set(killnextzodiacseq)))
            pass
        # 杀1肖
        killnextzodiac = jo[index][1]['six_number']['5']['zodiac']
        killnextzodiacseq = Common.getnumber(killnextzodiac, 'z')
        if __isfixedkillzodiac3:
            swq = list(set(swq) - (set(killnextzodiacseq)))
            pass
        # 杀1尾
        killnexttail = str(jo[index][1]['six_number']['1']['number'])[1]
        killnextzodiacseq = Common.getnumber(killnexttail, 't')
        if __isfixedkilltaill1:
            swq = list(set(swq) - (set(killnextzodiacseq)))
            pass
        '''
        执行公式杀的过程中，需要对不同的段位进行不同的排序，否则按照默认顺序是错误的
        '''
        # 杀1尾
        sn = Sortnumber.sort_number(jo[index], __formulakilltailsort)
        killnexttail = str(Common.tailavg(fr.funtal(sn)))
        killnexttailseq = Common.getnumber(killnexttail, 't')
        if __isformulakilltail1:
            swq = list(set(swq) - (set(killnexttailseq)))
            pass
        # 杀1头
        sn = Sortnumber.sort_number(jo[index], __formulakillheadsort)
        killnexthead = str(Common.headavg(fr.funhed(sn)))
        killnexttailseq = Common.getnumber(killnexthead, 'h')
        if __isformulakillhead1:
            swq = list(set(swq) - (set(killnexttailseq)))
            pass
        # 杀波色
        sn = Sortnumber.sort_number(jo[index], __formulakillcolorsort)
        killnextcolor = Common.color(fr.funclr(sn))
        killnexttailseq = Common.getnumber(killnextcolor, 'c')
        if __isformulakillcolor1:
            swq = list(set(swq) - (set(killnexttailseq)))
            pass
        # 杀单双
        sn = Sortnumber.sort_number(jo[index], __formulakillsingledoublesort)
        killsingledouble = Common.singleordouble(fr.funeob(sn))
        killsingledoubleseq = Common.getnumber(killsingledouble, 's')
        if __isformulakillsingledouble:
            swq = list(set(swq) - (set(killsingledoubleseq)))
            pass

        try:
            if swq.index(nextnumber) >= 0:
                r = r + 1
                maxright = maxright + 1
                lastsetright = lastsetright + 1
                lastsetrightarray.append(str(index + 2).zfill(3))
                if maxright > mr:
                    mr = maxright
        except:
            if maxright > mr:
                mr = maxright
            else:
                maxright = 0
            lastsetright = 0
            lastsetrightarray = []
            e = e + 1

    print('==============公式预杀==============')
    print('公式总计: ' + str(len(jo)) + '/' + str(len(jo) - 1))
    print('公式对错: ' + str(r) + '/' + str(e) + '/' + str(round((r / (len(jo) - 1)) * 100.0, 2)) + '%')
    print('最高连中: ' + str(mr) + '次')
    print('近期连中: ' + str(lastsetright) + '次')
    print('连中期数: ' + str(lastsetrightarray))
    return str(round((r / (len(jo) - 1)) * 100.0, 2))


def drawimage():
    rightcolor = '#9999ff'
    errorcolor = '#ff9999'

    mpl.rcParams['axes.titlesize'] = 14
    mpl.rcParams['axes.labelsize'] = 12
    mpl.rcParams['xtick.labelsize'] = 12
    mpl.rcParams['ytick.labelsize'] = 0
    mpl.rcParams['xtick.major.size'] = 0
    mpl.rcParams['ytick.major.size'] = 0
    
    # 设置图像信息
    fig = plt.figure(figsize=(16, 12), dpi=100)
    
    # 在231位置加入新的图
    ax = plt.subplot(331)
    ax.set_title('全年公式对错率(%)')
    labals = ['正确率\n' + str(collosion.yearrighterrorrate[0]),
              '错误率\n' + str(collosion.yearrighterrorrate[1]),]
    ax.pie(collosion.yearrighterrorrate, labels=labals, colors=[rightcolor,errorcolor])
    
    # 在232位置加入新图
    ax = plt.subplot(332)
    ax.set_title('全年公式每月对错数')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    # 在233位置加入新图
    ax = plt.subplot(333)
    ax.set_title('最近十期开奖结果')
    ax.set_xticklabels([])
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    
    
    # 在212位置加入新图
    ax = plt.subplot(312)
    # 生成x轴每个元素的位置   
    X = np.arange(len(collosion.yearrighterrordrawdataarray))
    # Y轴上面的数据
    Y1 = np.array(collosion.yearrighterrordrawdataarray)
    # 添加并设置柱状图样式
    bars = ax.bar(X, Y1, width=0.55, edgecolor='white')
    for bar,x, y in zip(bars, X, Y1):
        if x % 2 == 0:
            bar.set_color(rightcolor)
        else:
            bar.set_color(errorcolor)
            pass
    plot(X, Y1 + 5, color=rightcolor, linewidth=2.5, linestyle="--", label="正确次数")
    legend(loc='upper left')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data',0))
    ax.set_xticks(X)
    xticks = ax.set_xticklabels(Y1, fontsize=10)
    for xt, x,y in zip(xticks, X, Y1):
        if x % 2 == 0:
            xt.set_color(rightcolor)
        else:
            xt.set_color(errorcolor)

    # 在313位置加入新图
    ax = plt.subplot(313)
    ax.set_xticklabels([])
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    text(0, 0.8, '公式对错: ' + str(collosion.r) + '次/' + str(collosion.e) + '次', fontsize=14)
    text(0, 0.7, '最高连对: ' + str(collosion.mr) + '次', fontsize=14)
    text(0, 0.6, '最新连对: ' + str(collosion.lastsetright) + '次', fontsize=14)
    text(0, 0.5, '连对期数: ' + str(collosion.lastsetrightarray), fontsize=14)
    text(0, 0.4, '最高连错: ' + str(collosion.me) + '次', fontsize=14)
    text(0, 0.3, '最新连错: ' + str(collosion.lastseterror) + '次', fontsize=14)
    text(0, 0.2, '连错期数: ' + str(collosion.lastseterrorarray), fontsize=14)
    text(0, 0.1, '成本总计: ' + str(collosion.totalcost), fontsize=14)
    text(0, 0.0, '预计回报: ' + str(collosion.expectedreturn), fontsize=14)
    text(0, -0.175, '预测号码: [' +
            str(len(collosion.nextnumberlist)) + ']个号码 \n' + 
            str(collosion.nextnumberlist), fontsize=14)
    
    show()


main()


# http://blog.csdn.net/u011497262/article/details/52325705
