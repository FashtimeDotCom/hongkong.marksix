#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 该脚本用于抓取指定年份开始到结束的所有六合彩数据
# 包括：期数，开奖日期，开奖号码，特码，波色，号码对应生肖
# 需要库：urllib3，BeautifulSoup
# 作者：stevelee
# 版本：20171217

import json
import os
import urllib3
from bs4 import BeautifulSoup

__yearPath__ = 'http://www.44kj.com/44kj/history/'
__oriConts__ = '<html></html>'
__pageType__ = '.html'

__beginYear__ = 2000
__endYear__ = 2017

__allyeardata__ = []


# 抓取并处理每一期的所有数据
# td: 所有td表格数据BS4集合
def NumberPperiods(td):
    print('length:', len(td))

    __da = {}
    __iq = {}

    o = 0
    i = ''

    for t in td:

        o = o + 1
        if t != '\n':

            # 日期
            if len(t) == 1 and t.string.find('-') > 0:
                __iq['datetime'] = AtChar(t.string)

            # 开奖期数
            if str(t.next.string).find(u'\u671f') > 0:
                i = RepChar(str(t.next.string))

            # 开奖号码（6个）
            if len(t) == 4:
                num1 = ((t.contents[0]).contents[1]).contents[0]
                num2 = ((t.contents[0]).contents[2]).contents[0]
                num3 = ((t.contents[0]).contents[3]).contents[0]
                num4 = ((t.contents[0]).contents[4]).contents[0]
                num5 = ((t.contents[0]).contents[5]).contents[0]
                num6 = ((t.contents[0]).contents[6]).contents[0]
                zod1 = ((t.contents[0]).contents[1]).contents[1]
                zod2 = ((t.contents[0]).contents[2]).contents[1]
                zod3 = ((t.contents[0]).contents[3]).contents[1]
                zod4 = ((t.contents[0]).contents[4]).contents[1]
                zod5 = ((t.contents[0]).contents[5]).contents[1]
                zod6 = ((t.contents[0]).contents[6]).contents[1]
                six_number = {
                    1: {
                        'number': AtChar(num1.string),
                        'color': AtChar(num1['class'][1]),
                        'zodiac': AtChar(zod1.string)
                    },
                    2: {
                        'number': AtChar(num2.string),
                        'color': AtChar(num2['class'][1]),
                        'zodiac': AtChar(zod2.string)
                    },
                    3: {
                        'number': AtChar(num3.string),
                        'color': AtChar(num3['class'][1]),
                        'zodiac': AtChar(zod3.string)
                    },
                    4: {
                        'number': AtChar(num4.string),
                        'color': AtChar(num4['class'][1]),
                        'zodiac': AtChar(zod4.string)
                    },
                    5: {
                        'number': AtChar(num5.string),
                        'color': AtChar(num5['class'][1]),
                        'zodiac': AtChar(zod5.string)
                    },
                    6: {
                        'number': AtChar(num6.string),
                        'color': AtChar(num6['class'][1]),
                        'zodiac': AtChar(zod6.string)
                    }
                }
                __iq['six_number'] = six_number

            # 开奖特码
            if len(t) == 2:
                if len(t.next) == 5:
                    unusual_number = {
                        'number': AtChar((t.contents[0]).contents[1].string),
                        'color': AtChar(t.contents[0].contents[1]['class'][1]),
                        'zodiac': AtChar((t.contents[0]).contents[3].string)
                    }
                    __iq['unusual_number'] = unusual_number

        # 合并本tr数据
        if str(t.contents[0]).find('(') == 0 and str(t.contents[0]).find(
                ')') > 0:
            __da[i] = __iq
            __iq = {}

    print('total number is: ' + str(len(__da)))
    return __da


def HandleYearList():
    return range(__beginYear__, __endYear__ + 1)


# 请求数据
def RequestPageContent(link):
    response = urllib3.PoolManager().request('GET', link)
    __oriContent__ = response.data
    return __oriContent__


# 转换html字符
def ConvertSoupObject(c):
    return BeautifulSoup(c, "html.parser", from_encoding='gbk')


def OpenWiteFile(c, n):
    fo = open(os.getcwd() + "/records/" + str(n) + ".json", 'w', encoding='utf8')
    s = FormatJson(c, 4).encode('utf-8').decode('unicode_escape')
    fo.write(s)
    print(str(n) + ' year data writed completed')
    fo.close()


def openReadFile():
    fo = open(os.getcwd() + "/Files/sample.txt", 'r+')
    c = fo.read()
    fo.close()
    return c


def FormatJson(c, n=4):
    # if n > 0:
    #     return json.dumps(c, n)
    # else:
    return json.dumps(c)


def AtChar(c):
    return c.replace('BoClass', '')


def RepChar(c):
    return c.replace('\r', '').replace('\n', '').replace(' ', '').replace(
        '	', '')


def Main():
    year = HandleYearList()
    for y in year:
        link = __yearPath__ + str(y) + __pageType__

        print('begging spider ' + str(y) + ' web page data.')
        pageContent = RequestPageContent(link)
        print('spider data completed, data length: ' + str(len(pageContent)))

        soup = ConvertSoupObject(pageContent)
        print('at ' + str(y) + ' html data.')

        # 将数据填充到arraylist对象中
        data = NumberPperiods(soup.table.find_all('td'))

        OpenWiteFile(sorted(data.items(), key=lambda d: d[0]), y)

        __allyeardata__.append(sorted(data.items(), key=lambda d: d[0]))
        print('spider ' + str(y) + ' completed.')
        print('end')
        print()
    pass
    print('tranle to txt')
    alldata = ''
    for dt in __allyeardata__:
        for dd in dt:
            num1 = dd[1]['six_number'][1]['number']
            num2 = dd[1]['six_number'][2]['number']
            num3 = dd[1]['six_number'][3]['number']
            num4 = dd[1]['six_number'][4]['number']
            num5 = dd[1]['six_number'][5]['number']
            num6 = dd[1]['six_number'][6]['number']

            zic1 = dd[1]['six_number'][1]['zodiac']
            zic2 = dd[1]['six_number'][2]['zodiac']
            zic3 = dd[1]['six_number'][3]['zodiac']
            zic4 = dd[1]['six_number'][4]['zodiac']
            zic5 = dd[1]['six_number'][5]['zodiac']
            zic6 = dd[1]['six_number'][6]['zodiac']

            clr1 = dd[1]['six_number'][1]['color'][0]
            clr2 = dd[1]['six_number'][2]['color'][0]
            clr3 = dd[1]['six_number'][3]['color'][0]
            clr4 = dd[1]['six_number'][4]['color'][0]
            clr5 = dd[1]['six_number'][5]['color'][0]
            clr6 = dd[1]['six_number'][6]['color'][0]

            numn = dd[1]['unusual_number']['number']
            clrn = dd[1]['unusual_number']['color'][0]
            zicn = dd[1]['unusual_number']['zodiac']

            alldata = alldata + num1 + ',' + num2 + ',' + num3 + ',' + \
                      num4 + ',' + num5 + ',' + num6 + ',' + numn + ',' + \
                      clr1 + ',' + clr2 + ',' + clr3 + ',' + clr4 + ',' + \
                      clr5 + ',' + clr6 + ',' + clrn + ',' + zic1 + ',' + \
                      zic2 + ',' + zic3 + ',' + zic4 + ',' + zic5 + ',' + \
                      zic6 + ',' + zicn + ',\r\n'
            pass
    pass
    print(alldata)
    fo = open(os.getcwd() + "/records/allyeardata.txt", 'w', encoding='utf8')
    fo.write(alldata)
    fo.close()


pass

Main()
