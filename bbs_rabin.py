import random


def isPrime(n):
    return 2 in [n, 2**n%n]

def genPrime():
    return random.sample([i for i in range(1, 100) if isPrime(i) and i%4 == 3], 2)

def bbs():
    p, q = genPrime()
    s = random.randrange(1000000)
    n = p*q
    x = s*s % n
    b = ''
    for _ in range(16):
        x = x*x % n
        b += str(x%2)
    return int(b, 2)

def main():
    print(bbs())


if __name__ == '__main__':
    main()