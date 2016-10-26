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
        self.__key = [0]

    def setKey(self, key):
        self.__key = key

    def getKey(self):
        return self.__key

    def __generateMatrix(self, input, key):
        keyLength = len(key)
        input = input + 'X'*((keyLength - len(input)%keyLength) % keyLength)
        matrix = np.array([list(char) for char in input]).reshape(-1, keyLength)
        return matrix[:, np.argsort(key)]

    def encrypt(self, input):
        matrix = self.__generateMatrix(input, sorted(self.__key))
        return ''.join(matrix.flatten())

    def decrypt(self, input):
        matrix = self.__generateMatrix(input, self.__key)
        return ''.join(matrix.flatten())


if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = Transposition()

    message = raw_input('Enter your message: ')
    key = map(int, input('Enter the column permutation: ').split())

    # key = [4, 3, 1, 2, 5, 6, 7]
    # print(myObj.getKey())
    myObj.setKey(key)

    cipher = myObj.encrypt(message)
    print('Cipher Text: {}'.format(cipher))

    plain = myObj.decrypt(cipher)
    print('Plain Text: {}'.format(plain))