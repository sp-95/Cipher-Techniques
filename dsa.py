import random
from math import sqrt


def isPrime(n):
    return 2 in [n, pow(2, n, n)]

def genPrime(start, stop):
    return [i for i in range(start, stop) if isPrime(i)]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def genK(q):
    k = random.randrange(1, q)
    try:
        modinv(k, q)
        return k
    except:
        return genK(q)

def sign(p, q, g, x, k, H, M):
    r = pow(g, k, p) % q
    s = (modinv(k, q)*(H^M + x*r)) % q
    return r, s

def verify(p, q, g, y, H, M, r, s):
    w = modinv(s, q)
    u1 = (H^M*w) % q
    u2 = (r*w) % q
    v = ((pow(g, u1) * pow(y, u2)) % p) % q
    return v

def main():
    p = random.choice([genPrime(pow(2, i), pow(2, i+1)) for i in range(511, 1024, 64)])
    q = random.choice([i for i in range(pow(2, 159), pow(2, 160)) if isPrime(i) and (p-1) % q == 0])
    h = random.randrange(1, p-1)
    g = pow(h, (p-1) / q, p)
    while g <= 1:
        h = random.randrange(1, p-1)
        g = pow(h, (p-1) / q, p)

    print('p: {}'.format(p))
    print('q: {}'.format(q))
    print('g: {}'.format(g))

    x = random.randrange(1, q)
    y = pow(g, x, p)
    print('x: {}'.format(x))
    print('y: {}'.format(y))

    k = genK(q)
    print('k: {}'.format(k))
    
    M = random.getrandbits(320)
    print('M: {}'.format(M))
    H = random.getrandbits(320)
    print('Hash: {}'.format(H))

    r, s = sign(p, q, g, x, k, H, M)
    print('r: {}'.format(r))
    print('s: {}'.format(s))

    v = verify(p, q, g, y, H, M, r, s)
    print('v: {}'.format(v))

    if v == r:
        print('Verified')
    else:
        print('Verification failed')


if __name__=='__main__':
    main()