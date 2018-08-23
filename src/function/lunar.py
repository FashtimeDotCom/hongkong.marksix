#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src import mathevenorbill


def GetDayOf(st, format='Number'):

    #–天干名称
    cTianGan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

    #–地支名称
    cDiZhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

    #–属相名称
    cShuXiang = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]

    #–农历日期名
    cDayName = [
        "*", "初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一",
        "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三",
        "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"
    ]

    #–农历月份名
    cMonName = [
        "*", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "腊"
    ]

    #–公历每月前面的天数
    wMonthAdd = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    #– 农历数据
    wNongliData = [
        2635, 333387, 1701, 1748, 267701, 694, 2391, 133423, 1175, 396438,
        3402, 3749, 331177, 1453, 694, 201326, 2350, 465197, 3221, 3402,
        400202, 2901, 1386, 267611, 605, 2349, 137515, 2709, 464533, 1738,
        2901, 330421, 1242, 2651, 199255, 1323, 529706, 3733, 1706, 398762,
        2741, 1206, 267438, 2647, 1318, 204070, 3477, 461653, 1386, 2413,
        330077, 1197, 2637, 268877, 3365, 531109, 2900, 2922, 398042, 2395,
        1179, 267415, 2635, 661067, 1701, 1748, 398772, 2742, 2391, 330031,
        1175, 1611, 200010, 3749, 527717, 1452, 2742, 332397, 2350, 3222,
        268949, 3402, 3493, 133973, 1386, 464219, 605, 2349, 334123, 2709,
        2890, 267946, 2773, 592565, 1210, 2651, 395863, 1323, 2707, 265877
    ]

    #—取当前公历年、月、日—
    wCurYear = st["year"]
    wCurMonth = st["mon"]
    wCurDay = st["day"]

    #—计算到初始时间1921年2月8日的天数：1921-2-8(正月初一)—
    nTheDate = (wCurYear - 1921) * 365 + (
        wCurYear - 1921) / 4 + wCurDay + wMonthAdd[wCurMonth - 1] - 38
    if (((wCurYear % 4) == 0) and (wCurMonth > 2)):
        nTheDate = nTheDate + 1

    #–计算农历天干、地支、月、日—
    nIsEnd = 0
    m = 0
    while nIsEnd != 1:
        #if wNongliData[m+1] < 4095:
        if wNongliData[m] < 4095:
            k = 11
        else:
            k = 12
        n = k
        while n >= 0:
            nBit = wNongliData[m]
            for i in range(n):
                nBit = mathevenorbill.floor(nBit / 2)

            nBit = nBit % 2

            if nTheDate <= (29 + nBit):
                nIsEnd = 1
                break

            nTheDate = nTheDate - 29 - nBit
            n = n - 1

        if nIsEnd != 0:
            break
        m = m + 1

    wCurYear = 1921 + m
    wCurMonth = k - n + 1
    wCurDay = int(mathevenorbill.floor(nTheDate))
    if k == 12:
        if wCurMonth == wNongliData[m] / 65536 + 1:
            wCurMonth = 1 - wCurMonth
        elif wCurMonth > wNongliData[m] / 65536 + 1:
            wCurMonth = wCurMonth - 1

    if format == 'Number':
        return str(wCurYear) + "-" + str(wCurMonth) + "-" + str(wCurDay)
    else:
        
        #–生成农历天干、地支、属相 ==> wNongli–
        szShuXiang = cShuXiang[(((wCurYear - 4) % 60) % 12) + 1]
        szShuXiang = cShuXiang[(((wCurYear - 4) % 60) % 12) + 1]
        zNongli = szShuXiang + '(' + cTianGan[((
            (wCurYear - 4) % 60) % 10)] + cDiZhi[((
                (wCurYear - 4) % 60) % 12)] + ')年'

        if wCurMonth < 1:
            szNongliDay = "闰" + cMonName[(-1 * wCurMonth)]
        else:
            szNongliDay = cMonName[wCurMonth]

        szNongliDay = szNongliDay + "月" + cDayName[wCurDay]
        print(szNongliDay)
        #return szNongli .. szNongliDay
        return szNongliDay

# def main():
    
#     st1 = {"year": 2017, "mon": 9, "day": 13}
#     print GetDayOf(st1)

# main()