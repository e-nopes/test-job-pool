#!/usr/bin/env python3

import threading, queue
import time

class JobPool():
    def __init__(self, number_of_workers):
        
        self.q = queue.Queue()
        self.active = True
        for i in range(number_of_workers):
            threading.Thread(target=self.worker, daemon=True, args=(i,) ).start()

    def addJob(self, num):
        if self.active:
            message = f'\n--I am Process {num}--'
            self.q.put( message )

    def stop(self):
        self.active=False
        return self.q.join()

    def worker(self, number):
        while self.active:
            print(f'Thread {number} started...')

            item = self.q.get()
            print(f'Working on {item}')
            time.sleep(5)
            print(f'Finished {item}')
            self.q.task_done()



pool = JobPool(10)
print('Created pool')
pool.addJob(1)
pool.addJob(2)
pool.addJob(3)

print('All task requests sent')

pool.stop()

print('All work completed')