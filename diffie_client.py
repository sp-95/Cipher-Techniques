import socket
import random


def isPrime(n):
    return 2 in [n, pow(2, n, n)]

def genPrime():
    return random.choice([i for i in range(1, 100) if isPrime(i)])

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 3000

    s.connect((host, port))
    q = genPrime()
    print('q: {}'.format(q))
    alpha = random.randrange(1000)
    print('alpha: {}'.format(alpha))
    xa = random.randrange(1000)
    print('xa: {}'.format(xa))

    s.send('{} {}'.format(q, alpha))
    ya = pow(alpha, xa, q)
    print('ya: {}'.format(ya))

    yb = int(s.recv(1024))
    print('yb: {}'.format(ya))
    s.send(str(ya))
    
    k = pow(yb, xa, q)
    print('k: {}'.format(k))
    s.close()


if __name__ == '__main__':
    main()