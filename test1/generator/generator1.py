def create_sum(all_num):
    a, b = 0, 1
    idx = 0
    while idx < all_num:
        # print(a)
        yield a  # 如果一个函数中有yield语句，
        a, b = b, a + b
        idx += 1


obj = create_sum(10)

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

# for x in obj:a
#     print(x)
