def create_sum(all_num):
    a, b = 0, 1
    idx = 0
    while idx < all_num:
        # print(a)
        ret = yield a  # 如果一个函数中有yield语句，
        print(">>>>>ret>>>>", ret)
        a, b = b, a + b
        idx += 1
    return "ok..."


obj = create_sum(10)

ret = obj.send(None)
print(ret)

ret = next(obj)
print(ret)

ret = obj.send("haha")
print(ret)

ret = obj.send("haha")
print(ret)

ret = obj.send("haha")
print(ret)
