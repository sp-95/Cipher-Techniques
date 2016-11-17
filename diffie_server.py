import socket
import random


def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 3000
    s.bind((host, port))

    s.listen(5)
    c, addr = s.accept()

    xb = random.randrange(1000)
    q, alpha = map(int, c.recv(1024).split())
    print('q: {}'.format(q))
    print('alpha: {}'.format(alpha))
    yb = pow(alpha, xb, q)
    print('yb: {}'.format(yb))
    c.send(str(yb))
    ya = int(c.recv(1024))
    print('ya: {}'.format(ya))
    k = pow(ya, xb, q)
    print('k: {}'.format(k))
    c.close()


if __name__ == '__main__':
    main()