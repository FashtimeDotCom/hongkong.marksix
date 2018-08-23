#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import *
from multiprocessing.managers import BaseManager
from job import Job


class Master:

    def __init__(self):
        # 派发出去的作业队列
        self.dispatched_job_queue = Queue()
        # 完成的作业队列
        self.finished_job_queue = Queue()

    def get_dispatched_job_queue(self):
        return self.dispatched_job_queue

    def get_finished_job_queue(self):
        return self.finished_job_queue

    def start(self):
        # 把派发作业队列和完成作业队列注册到网络上
        BaseManager.register('get_dispatched_job_queue', callable=self.get_dispatched_job_queue)
        BaseManager.register('get_finished_job_queue', callable=self.get_finished_job_queue)

        # 监听端口和启动服务
        manager = BaseManager(address=('127.0.0.1', 8888), authkey=b'jobs')
        manager.start()

        # 使用上面注册的方法获取队列
        dispatched_jobs = manager.get_dispatched_job_queue()
        finished_jobs = manager.get_finished_job_queue()

        # 这里一次派发10个作业，等到10个作业都运行完后，继续再派发10个作业
        job_id = 0
        while True:
            for i in range(0, 10):
                job_id = job_id + 1
                job = Job(job_id)
                print('Dispatch job: %s' % job.job_id)
                dispatched_jobs.put(job)

            while not dispatched_jobs.empty():
                job = finished_jobs.get(60)
                print('Finished Job: %s' % job.job_id)

        manager.shutdown()

if __name__ == "__main__":
    master = Master()
    master.start()