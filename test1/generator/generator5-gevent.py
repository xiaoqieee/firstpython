import gevent


def task(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.001)


g1 = gevent.spawn(task, 5)
g2 = gevent.spawn(task, 5)
g3 = gevent.spawn(task, 5)

g1.join()
g2.join()
g3.join()
