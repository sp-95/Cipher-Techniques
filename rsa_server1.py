import socket


def main():
    s = socket.socket()
    host = s.gethostname()
    port = 3000

    s.bind((host,port))

    s.listen(5)
    c, addr = s.accept()
    s.close()


if __name__ == '__main__':
    main()