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
        self.__columnPermutation = [0]

    def setKey(self, key):
        pass

    def getKey(self):
        return self.key

    def encrypt(self, input):
        pass

    def decrypt(self, input):
        pass


if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = Transposition()

    message = raw_input('Enter your message: ')
    key = map(int, input('Enter the column permutation: ').split())

    cipher = myObj.encrypt(message)
    print('Cipher Text: {}'.format(cipher))

    plain = myObj.decrypt(cipher)
    print('Plain Text: {}'.format(plain))