import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("-----%d-----" % i)
            time.sleep(0.5)


def main():
    t = MyThread()
    t.start()


if __name__ == '__main__':
    main()
