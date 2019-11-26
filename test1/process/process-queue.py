from multiprocessing import Process
from multiprocessing import Queue
import time


def download(q):
    data = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    for d in data:
        q.put(d)
        print("-----下载数据[%d]-----" % d)
        time.sleep(1)
    print("-----下载数据完毕-----")


def analysis(q):
    while True:
        d = q.get()
        print("-----处理数据[%d]-----" % d)


def main():
    q = Queue(3)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=analysis, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
