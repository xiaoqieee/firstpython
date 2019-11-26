from collections.abc import Iterable
from collections.abc import Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)


class ClassIterator(object):

    def __init__(self, obj):
        self.obj = obj
        self.idx = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.idx < len(self.obj.names):
            r = self.obj.names[self.idx]
            self.idx += 1
            return r
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

# print(isinstance(classmate, Iterable))
# classmate_iter = iter(classmate)
# print(isinstance(classmate_iter, Iterator))
# print(next(classmate_iter))


for name in classmate:
    print(name)
    time.sleep(0.5)
