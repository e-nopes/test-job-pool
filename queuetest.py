#!/usr/bin/env python3

import threading, queue
import time

class JobPool():
    def __init__(self, number_of_workers):
        
        self.q = queue.Queue(number_of_workers)
        self.active = True
        for i in range(number_of_workers):
            threading.Thread(target=self.worker, daemon=True, args=(i,) ).start()

    def addJob(self, a,b ):
        if self.active:
            self.q.put( a  )

    def stop(self):
        if self.active:
            return self.q.join()
    

    def worker(self, number ):
        while self.active:
            print(f'Thread {number} .')

            item = self.q.get()
            print(f'Working on {item}')
            time.sleep(5)
            print(f'{number} Finished {item}')
            self.q.task_done()



pool = JobPool(4)
print('Created pool')
pool.addJob('a.txt','1.txt')
pool.addJob('b.txt','2.txt')
pool.addJob('c.txt','3.txt')
pool.addJob('d.txt','4.txt')

pool.addJob('e.txt','5.txt')


print('All task requests sent')

pool.stop()

print('All work completed')
