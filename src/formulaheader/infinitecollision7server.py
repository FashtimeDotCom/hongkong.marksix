#!/usr/bin/env python
# coding=utf-8


import numpy as np
import time, threading, sys, os
from multiprocessing import *
from multiprocessing.managers import BaseManager
from itertools import *


class Master:
    # 服务端    
    stepstart = 5
    stepstop = 7
    # 计算阶长度(最长7阶---9618546700组公式)
    order = 7
    totalformal = 9618546700
    # 取数方式：      头 | 尾 | 原 | 合 | 积   
    getnumbertype = ['h', 't', 'o', 'j', 'a']
    # 随机偏移量(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    originoffsets = np.arange(0, 10)
    # 原始数据内容
    originnumbers = np.arange(0, 7)
    # 排序方式
    originsorttype = ['size', 'nosize']
    # new ----> server config
    # serverip = '61.152.104.186'
    serverip = '127.0.0.1'
    serverport = 1213
    serverauth = bytes('a.j2JI)', 'utf8')

    # 公式入队延时时间
    queuedispatchedsleep = 1.000
    # 结果出队延时时间
    queuefinishedsleep = 0.0

    # # 公式队列满时延时（1小时）
    # _queuedispatchedfullsleep = 1 * 60 * 60
    # queuedispatchedfullsleep = 0
    # # 结果列队满时延时（1小时）
    # _queuefinishedfullsleep = 1 * 60 * 60
    # queuefinishedfullsleep = 0

    def __init__(self):
        try:
            print('server is running...')
            self.dispatched_sequence_queue = Queue()
            self.finished_sequence_queue = Queue()
            BaseManager.register('get_dispatched_sequence_queue', callable=self.get_dispatched_sequence_queue)
            BaseManager.register('get_finished_sequence_queue', callable=self.get_finished_sequence_queue)
            self.manager = BaseManager(address=(self.serverip, self.serverport), authkey=self.serverauth)
            self.manager.start()
        except Exception as ex:
            print(ex)

    def math_inner_queue(self):
        count = 0
        dispatched_jobs = self.manager.get_dispatched_sequence_queue()
        # 罗列计算阶的长度
        for length in range(self.stepstart, self.stepstop + 1):
            # 获取数字排序集合
            pernumbercollection = [p for p in permutations(self.originnumbers, length)]
            # 获取字母排序集合
            itercollection = [''.join(x) for x in product(*[self.getnumbertype] * length)]
            # 存储生成的公式到队列
            for pernumber in pernumbercollection:
                for it in itercollection:
                    i = 0
                    fe = ''
                    for p in list(pernumber):
                        f = (str(p) + it[i])
                        fe += f + ' '
                        i += 1
                    fe = fe[0:len(fe) - 1]
                    for offset in self.originoffsets:
                        for sort in self.originsorttype:
                            count += 1
                            expression = {}
                            expression['expression'] = fe
                            expression['offset'] = offset
                            expression['sort'] = sort
                            dispatched_jobs.put(expression)
                    time.sleep(self.queuedispatchedsleep)

        print('\nqueue math is completed!')
        print('total math number: %s' % count)

    def get_current_queue_size(self):
        '''
        分析当前公式队列
        该函数只对公式队列进行剩余数量分析，不进行FIFO操作
        :return: 
        '''
        dispatched_jobs = self.manager.get_dispatched_sequence_queue()
        while True:
            try:
                time.sleep(1)
                if dispatched_jobs.qsize() <= 0:
                    print('queue empty')
                if dispatched_jobs.full():
                    print('dispatched queue full')
                self._print(
                    'Surplus formula number: %s' %
                    (self.totalformal - (self.totalformal - dispatched_jobs.qsize())))
            except Exception as ex:
                self.writefile('get_current_queue_size', str(ex) + '\n' +
                               'dispatched queue count:' + dispatched_jobs.qsize())
                pass

    def get_result_queue(self, killtype):
        '''
        分析当前结果列队
        该函数对结果队列进行分析，且进行FIFO操作，因此如果积压队列数量过多，同样会造成内存不足
        因此，该出队操作不应该有延迟
        :param killtype: 
        :return: 
        '''
        finished_jobs = self.manager.get_finished_sequence_queue()
        rat = 0
        while True:
            try:
                if finished_jobs.full():
                    print('finished queue full')

                result = finished_jobs.get()
                if result['rat'] > rat:
                    rat = result['rat']
                    print('=>current rate: ' + str(rat) + '%, exp:' + str(result['exp']))
                    self.writefile(killtype, str(result))
                time.sleep(self.queuefinishedsleep)
            except Exception as ex:
                if finished_jobs.qsize() > 0:
                    self.writefile('get_result_queue', str(ex) + '\n' +
                                   'finished queue count:' + finished_jobs.qsize())
                pass

    def get_dispatched_sequence_queue(self):
        return self.dispatched_sequence_queue

    def get_finished_sequence_queue(self):
        return self.finished_sequence_queue

    def _print(self, s):
        sys.stdout.write("\r" + s)
        sys.stdout.flush()

    def writefile(self, filename, content):
        fo = open(os.getcwd() + "/" + filename + ".txt", 'w', encoding='utf8')
        fo.write(content)
        fo.close()


if __name__ == '__main__':
    master = Master()
    threading.Thread(target=master.math_inner_queue).start()
    threading.Thread(target=master.get_current_queue_size).start()
    threading.Thread(target=master.get_result_queue, args=('killtail',)).start()
