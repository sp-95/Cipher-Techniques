"""'
Transposition Cipher
=============

Input:
    Input string and column permutation as key

Output:
    Encrypted and Decrypted strings using Columnar Trasposition Cipher
"""

import __future__


__author__ = 'Shashanka Prajapati'


import numpy as np


class Transposition:
    def __init__(self):
        self.__encryptionKey = [0]
        self.__decryptionKey = [0]

    def setKey(self, key):
        self.__encryptionKey = np.array(key)
        self.__decryptionKey = np.argsort(self.__encryptionKey)

    def getKey(self):
        return list(self.__encryptionKey) 

    def encrypt(self, input):
        keyLength = len(self.__encryptionKey)
        input = input + 'X'*((keyLength - len(input)%keyLength) % keyLength)    # Padding to fill the matrix
        matrix = self.__toList(input).reshape(-1, keyLength)
        cipher = matrix[:, np.argsort(self.__encryptionKey)]
        return ''.join(cipher.T.flatten())

    def decrypt(self, input):
        matrix = self.__toList(input).reshape(-1, len(input)//len(self.__decryptionKey)).T
        plain = matrix[:, np.argsort(self.__decryptionKey)]
        return ''.join(plain.flatten())

    def __toList(self, string):
        return np.array([list(char) for char in string])

if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = Transposition()

    message = raw_input('Enter your message: ')
    # key = map(int, raw_input('Enter the column permutation: ').split())

    key = [4, 3, 1, 2, 5, 6, 7]
    myObj.setKey(key)
    print(myObj.getKey())

    cipher = myObj.encrypt(message)
    print('Cipher Text: {}'.format(cipher))

    plain = myObj.decrypt(cipher)
    print('Plain Text: {}'.format(plain))