import re


def main():
    while True:
        email = input("请输入邮箱地址：")
        ret = re.match(r"^[a-zA-Z_0-9]+\w{2,19}@163\.com", email)
        if ret:
            print("[%s]符合规则" % email)
        else:
            print("[%s]不符合规则" % email)


if __name__ == '__main__':
    main()
