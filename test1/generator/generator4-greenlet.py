from greenlet import greenlet
import time


def task_1():
    while True:
        print("----1---")
        time.sleep(0.5)
        gr2.switch()


def task_2():
    while True:
        print("----2---")
        time.sleep(0.5)
        gr3.switch()


def task_3():
    while True:
        print("----3---")
        time.sleep(0.5)
        gr4.switch()


def task_4():
    while True:
        print("----4---")
        time.sleep(0.5)
        gr1.switch()


gr1 = greenlet(task_1)
gr2 = greenlet(task_2)
gr3 = greenlet(task_3)
gr4 = greenlet(task_4)

gr1.switch()
