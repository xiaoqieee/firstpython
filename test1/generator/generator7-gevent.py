import gevent
from gevent import monkey
import time

monkey.patch_all()


def task(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        time.sleep(0.001)


gevent.joinall([
    gevent.spawn(task, 5),
    gevent.spawn(task, 5),
    gevent.spawn(task, 5)
])
