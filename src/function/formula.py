#!/usr/bin/env python
# coding=utf-8

from function.common import Common
from function.common import SortNumber

sortnumber = SortNumber()


def formulakillsingleordouble(s):
    # 单双公式 （错误率太高，正确率太低，pass）
    # 62
    return Common.get(s[1], 't') + \
           Common.get(s[2], 't') + \
           Common.get(s[3], 'j') + \
           Common.get(s[4], 'j') + \
           Common.get(s[5], 'j') + 2

    # 53.33
    # return Common.get(s[1], 'h') + \
    #        Common.get(s[2], 'h') + \
    #        Common.get(s[3], 'h') + \
    #        Common.get(s[4], 'h') + \
    #        Common.get(s[5], 'h') + 1


def formulakillcolor(s):
    # 波色公式 
    # 72
    # return Common.get(s[2], 'j') + \
    #        Common.get(s[3], 't') + \
    #        Common.get(s[4], 'j') + \
    #        Common.get(s[5], 't') + \
    #        Common.get(s[6], 't') + 1
    # 153
    # 76.97
    # 6j 4o 1o 6h 6o 4o 2h 3h 6h 2h 3j 4hj 5t 5j 2t 1t 3t 3t
    # 79.61
    # 0t 0h 1j 1h 1t 2o 1h 1t 3t 3t 2h 2j
    # 80.26
    # 0h 0o 0t 1j 1t 1o 0t 0t 0j 0j 0o offset: 3
    # 80.92
    # 1j 4h 1j 3h 3j 4j 6j 4j 4o 3t 6t 5t 2t 6h 0h 3h 4t 3j 2j 2t 3o 4t 5o 0o 3j 1h 1o 6j 6j 1o 6h 3o 6t 5t 1j 5h 4o 4h 1o 2j 2t 0t 3j 1t 1h 2o 6j 4j 0j 4t 4j 3j 3o 2j 1t 6o 1h 1t 4j 2j 5j 6o 0o 3o 5t 1t 1t 5o 3o 5j 3h 0t 3o 4h 3o 3t 2t 5t 5j 2h 5t 5h 6t 6h 4t 6t 0t 4t 0t 5h 3o 6h 0h 6h 0h offset: 0
    # 83.55
    # 2j 2h 1j 0t 1j 1t 1h 2t 2t 0o 0j 0h 0t 2j 0t 0j 2o 1j 0j 1h 2t 2h 2o 2h 2t 2t 2j 2h 2h 0t 1h 2t 0j 2t 2o 2j 0h 1t 1o 2t 2h 0t 1h 2o 0o offset: 0 sorttype: 0
    # 82.89
    # 3o 3o 2o 0j 2h 0j 0h 1t 1o offset: 12
    # 84.87
    # 0j 1t 0h 1h 0t 1h 1h 1t 1h 1t 1j 1j 0j 0o 1j 1h 0t 1h 1t 0j offset: 1

    # 2700
    # 83.67%
    # 2j 2t 1h 0t 3o 5t 2t 1h 3j 0h 5t 4t 4t 5h 2t 2t 2t 1o 2o 5o 3j 0t 4j 3t 4j 4t 3j 2o 0j 1h 3t 1t 4o 4o 5j 2h 3o 2h 2h 0o offset: 6 sorttype: nosize
    # 73.68
    return Common.get(s[2], 'h') + \
           Common.get(s[3], 'j') + \
           Common.get(s[4], 'h') + \
           Common.get(s[5], 'j') + \
           Common.get(s[6], 'j') + 1


def formulakilltail(sn):
    """
    公式杀尾
    :return: 
    """
    # { 'pid': 33631, 'exp': {'offset': 4, 'expression': '0h 1t 3t 4h 5a', 'sort': 'nosize'}, 'rat': 92.142 }
    formula = {"expression": "0h 1t 3t 4h 5a", "offset": 4, "sorttype": "nosize"}

    killtail = Common.tail(Common.formula_expression_hander(formula['expression'],
                                                            sortnumber.sort_number(sn, formula['sorttype']),
                                                            formula['offset'])[0])
    return Common.getnumber(str(killtail), 't')


def formulakillhead(s):
    # 杀头公式 (4个头)
    # 85.33%
    # return Common.get(s[0], 't') + \
    #        Common.get(s[1], 't') + \
    #        Common.get(s[2], 'j') + \
    #        Common.get(s[3], 'j') + \
    #        Common.get(s[4], 'j') + 3

    # 90.0%
    return Common.get(s[0], 't') + \
           Common.get(s[1], 't') + \
           Common.get(s[2], 't') + \
           Common.get(s[3], 'j') + \
           Common.get(s[4], 'j') + 5
