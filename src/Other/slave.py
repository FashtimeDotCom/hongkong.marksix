#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os
from multiprocessing.managers import BaseManager
from job import Job


class Slave:

    def start(self):
        # 把派发作业队列和完成作业队列注册到网络上
        BaseManager.register('get_dispatched_job_queue')
        BaseManager.register('get_finished_job_queue')

        # 连接master
        server = '127.0.0.1'
        print('Connect to server %s...' % server)
        manager = BaseManager(address=(server, 8888), authkey=bytes('jobs', 'utf8'))
        manager.connect()

        # 使用上面注册的方法获取队列
        dispatched_jobs = manager.get_dispatched_job_queue()
        finished_jobs = manager.get_finished_job_queue()

        # 运行作业并返回结果，这里只是模拟作业运行，所以返回的是接收到的作业
        while True:
            job = dispatched_jobs.get(timeout=1)
            print('pid is [' + str(os.getpid()) + '], Run job: %s ' % job.job_id)
            time.sleep(0.5)
            finished_jobs.put(job)


if __name__ == "__main__":
    Slave().start()
