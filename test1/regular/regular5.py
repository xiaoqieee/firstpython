import re

ret = re.search(r"\d+", "月度次数为 99999 fdasfdsaf 88888")
print(ret.group())


ret = re.findall(r"\d+", "月度次数为 99999 fdasfdsaf 88888")
print(ret)

ret = re.sub(r"\d+", "998", "python=997,999")
print(ret)
