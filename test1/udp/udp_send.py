import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)

    while True:

        send_data = input("请输入...\n")

        if send_data == "exit":
            break

        # udp_socket.sendto(b"hahahahah", ("127.0.0.1", 8000))
        udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", 8080))

    udp_socket.close()


if __name__ == '__main__':
    main()
