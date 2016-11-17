import random


def isPrime(n):
    return 2 in [n, pow(2, n, n)]

def genPrime():
    return random.sample([i for i in range(1, 100) if isPrime(i) and i%4 == 3], 2)

def bbs():
    p, q = genPrime()
    s = random.randrange(1000000)
    n = p*q
    x = pow(s, 2, n)
    b = ''
    for _ in range(16):
        x = pow(x, 2, n)
        b += str(x%2)
    return int(b, 2)

def rabinMiller(n, p):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    k, q = 0, n - 1
    while q % 2 == 0:
        k += 1
        q //= 2

    for _ in range(p):
        a = random.randrange(2, n-1)
        x = pow(a, q, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(k - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    n = bbs()
    print('{} is {}Prime'.format(n, '' if rabinMiller(n, 5) else 'not '))


if __name__ == '__main__':
    main()