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
        """Initialize the column permutation"""
        self.__key = [0]

    def setKey(self, key):
        """Set the key"""
        self.__key = np.array(key)

    def getKey(self):
        """Get the key"""
        return list(self.__key) 

    def encrypt(self, input):
        """Encryption"""
        keyLength = len(self.__key)
        input = input + 'X'*((keyLength - len(input)%keyLength) % keyLength)    # Padding to fill the matrix
        matrix = self.__toList(input).reshape(-1, keyLength)
        cipher = matrix[:, np.argsort(self.__key)]
        return ''.join(cipher.T.flatten())

    def decrypt(self, input):
        """Decryption"""
        matrix = self.__toList(input).reshape(-1, len(input)//len(self.__key)).T
        plain = matrix[:, np.argsort(np.argsort(self.__key))]
        return ''.join(plain.flatten())

    def __toList(self, string):
        """Convert a string to list of characters"""
        return np.array([list(char) for char in string])

if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = Transposition()

    message = raw_input('Enter your message: ')

    # print('Enter the column permutation: ')
    # key = map(int, raw_input().split())
    # myObj.setKey(key)

    key = [4, 3, 1, 2, 5, 6, 7]
    myObj.setKey(key)
    print('Column Permutation:')
    print(myObj.getKey())

    cipher = myObj.encrypt(message)
    print('Cipher Text: {}'.format(cipher))

    plain = myObj.decrypt(cipher)
    print('Plain Text: {}'.format(plain))