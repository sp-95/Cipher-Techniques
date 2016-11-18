def initS(key):
    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def genStream(S):
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]
        yield K

def toAscii(s):
    return [ord(c) for c in s]


def rc4(key):
    S = initS(key)
    return genStream(S)

def main():
    # ciphertext should be BBF316E8D940AF0AD3
    key = 'Key'
    plaintext = 'Plaintext'

    # ciphertext should be 1021BF0420
    #key = 'Wiki'
    #plaintext = 'pedia'

    # ciphertext should be 45A01F645FC35B383552544B9BF5
    #key = 'Secret'
    #plaintext = 'Attack at dawn'
    key = toAscii(key)
    keystream = rc4(key)

    ciphertext = ''.join(['{:02X}'.format(ord(c)^keystream.next()) for c in plaintext])
    print(ciphertext)


if __name__ == '__main__':
    main()