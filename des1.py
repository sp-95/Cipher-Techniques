"""
DES Part 1
==========

Input:
    64-bit input and 48-bit key

Output:
    48-bit input for S-box
"""

import __future__


__author__ = 'Shashanka Prajapati'


import re
import numpy as np


class DESKeyError(Exception):
    """Exception class for DES Key Algorithm"""
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


class DESKey:
    def __init__(self):
        """Initialize plain text, key and the expansion permutation"""
        self.__plainText = '0101101000000000010110100000000000111100111100000011110000001111'
        self.__key = '011110000011001111000011001000001101101001110000'
        self.__e = [
            31, 0, 1, 2, 3, 4,
            3, 4, 5, 6, 7, 8,
            7, 8, 9, 10, 11, 12,
            11, 12, 13, 14, 15, 16,
            15, 16, 17, 18, 19, 20,
            19, 20, 21, 22, 23, 24,
            23, 24, 25, 26, 27, 28,
            27, 28, 29, 30, 31, 0,
            ]

    def setKey(self, key):
        """Set the 48-bit key"""
        if re.search('[^01]', key):
            raise DESKeyError('Key should contain only bits(0\'s and 1\'s)')
        if len(key) != 48:
            raise DESKeyError('Only 48-bit keys are accepted')
        self.__key = key

    def getKey(self):
        """Get the 48-bit key"""
        return self.__key

    def getPlainText(self):
        """Get the 64-bit plain text"""
        return self.__plainText

    def __expand(self, input):
        """Expand the 32-bit R to 48-bits"""
        return ''.join(np.array([c for c in input]).take(self.__e))

    def __exor(self, input):
        """XOR the expanded bits with the key"""
        return str(bin(int(input, 2)^int(self.__key, 2)))[2:]

    def encrypt(self, input=None):
        """Get the input for S-box"""
        if input is not None:
            if re.search('[^01]', input):
                raise DESKeyError('PlainText should contain only bits(0\'s and 1\'s)')
            if len(input) != 64:
                raise DESKeyError('Only 64-bit PlainTexts are accepted')
            self.__plainText = input
            return self.__exor(self.__expand(input[32:]))
        else:
            return self.__exor(self.__expand(self.__plainText[32:]))



if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = DESKey()

    # key = raw_input('Enter the 48-bit key: ')
    # myObj.setKey(key)

    print('Key: {}'.format(myObj.getKey()))

    # plain = raw_input('Enter the 64-bit PlainText: ')
    # print('Input for S-box: {}'.format(myObj.encrypt(plain)))

    print('Plain Text: {}'.format(myObj.getPlainText()))
    print('Input for S-box: {}'.format(myObj.encrypt()))