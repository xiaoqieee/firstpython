import multiprocessing
import os
import random
import time


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


def main():
    pool = multiprocessing.Pool(3)
    for i in range(10):
        pool.apply_async(worker, (i,))
    print("-------start--------")
    pool.close()
    pool.join()
    print("-------end----------")


if __name__ == '__main__':
    main()
