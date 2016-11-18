import socket
import ast


def encrypt(public, plaintext):
    key, n = public
    return [pow(ord(char), key, n) for char in plaintext]

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 3000

    s.bind((host,port))

    s.listen(5)
    c, addr = s.accept()

    public = ast.literal_eval(c.recv(1024))
    print('PU: {}'.format(public))
    c.send('ACK')

    plaintext = c.recv(1024)
    print('PlainText: {}'.format(plaintext))

    cipher = encrypt(public, plaintext)
    print('Cipher: {}'.format(' '.join(map(str, cipher))))
    c.send(str(cipher))

    c.close()
    s.close()


if __name__ == '__main__':
    main()