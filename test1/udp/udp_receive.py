import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)

    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))

    udp_socket.close()


if __name__ == '__main__':
    main()
