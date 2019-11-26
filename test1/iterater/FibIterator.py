class FibIterator(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.a = 0
        self.b = 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return ret
        else:
            raise StopIteration


fibo = FibIterator(2000)

for num in fibo:
    print(num)
