import re

ret = re.match(r"^([a-zA-Z_0-9]+\w{2,19})@(163|126|sina)\.com", "fengqi3389@sina.com")
print(ret.group(1))
print(ret.group(2))

html_str = "<h1>hahahaha</h1>"
ret = re.match(r"<(\w*)>.*</\1*>", html_str).group()
print(ret)

html_str = "<body><h1>hahahaha</h1></body>"
ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", html_str)
print(ret.group())
print(ret.group(1))
print(ret.group(2))


html_str = "<body><h1>hahahaha</h1></body>"
ret = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>", html_str)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
