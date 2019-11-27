import time


def task_1():
    while True:
        print("----1---")
        time.sleep(0.1)
        yield


def task_2():
    while True:
        print("----2---")
        time.sleep(0.1)
        yield


def task_3():
    while True:
        print("----3---")
        time.sleep(0.1)
        yield


def task_4():
    while True:
        print("----4---")
        time.sleep(0.1)
        yield


def main():
    t1 = task_1()
    t2 = task_2()
    t3 = task_3()
    t4 = task_4()
    while True:
        next(t1)
        next(t2)
        next(t3)
        next(t4)


if __name__ == '__main__':
    main()
