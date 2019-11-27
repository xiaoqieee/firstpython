import re

names = ["age", "_age", "age#", "age!", "a!ge", "a_ge", "1age", "a1ge", "a_ge", "____"]

for name in names:
    ret = re.match(r"^[a-zA-Z_]+\w*$", name)
    if ret:
        print("%s符合规则" % name)
    else:
        print("%s不符合规则" % name)
