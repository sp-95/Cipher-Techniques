import random
import fractions


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

def isPrime(n):
    return 2 in [n, pow(2, n, n)]

def genPrime():
    return random.sample([i for i in range(1, 100) if isPrime(i)], 2)

def genKey(p, q):
    n = p*q
    print('n: {}'.format(n))
    phi = (p - 1)*(q - 1)
    print('phi: {}'.format(phi))

    e = random.choice([i for i in range(1,phi) if fractions.gcd(i, phi) == 1])
    print('e: {}'.format(e))
    d = modinv(e, phi)
    print('d: {}'.format(d))
    
    return ((e, n), (d, n))

def encrypt(public, plaintext):
    key, n = public
    return [pow(ord(char), key, n) for char in plaintext]

def decrypt(private, cipher):
    key, n = private
    return ''.join([chr(pow(char, key, n)) for char in cipher])

def main():
    p, q = genPrime()
    print('p: {}'.format(p))
    print('q: {}'.format(q))

    public, private = genKey(p, q)
    print('PU: {}'.format(public))
    print('PR: {}'.format(private))

    plaintext = 'How are you?'
    print('PlainText: {}'.format(plaintext))

    cipher = encrypt(public, plaintext)
    print('Cipher: {}'.format(' '.join(map(str, cipher))))

    print('Decrypted Text: {}'.format(decrypt(private, cipher)))

if __name__ == '__main__':
    main()