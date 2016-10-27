"""
DES Key Algorithm
=================

Input:
    64-bit key

Output:
    48-bit keys for 16 rounds of DES Algorithm
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
        """Initialize key and the permutation choices"""
        self.__key = '0000111100010101011100011100100101000111110110011110100001011001'
        self.__pc1 = [
            [56, 48, 40, 32, 24, 16, 8],
            [0, 57, 49, 41, 33, 25, 17],
            [9, 1, 58, 50, 42, 34, 26],
            [18, 10, 2, 59, 51, 43, 35],
            [62, 54, 46, 38, 30, 22, 14],
            [6, 61, 53, 45, 37, 29, 21],
            [13, 5, 60, 52, 44, 36, 28],
            [20, 12, 4, 27, 19, 11, 3],
            ]
        self.__pc2 = [
            [13, 16, 10, 23, 0, 4, 2, 27],
            [14, 5, 20, 9, 22, 18, 11, 3],
            [25, 7, 15, 6, 26, 19, 12, 1],
            [40, 51, 30, 36, 46, 54, 29, 39],
            [50, 44, 32, 47, 43, 48, 38, 55],
            [33, 52, 45, 41, 49, 35, 28, 31],
            ]

    def setInitialKey(self, key):
        """Set the initial key"""
        if re.search('[^01]', key):
            raise DESKeyError('Key should contain only bits(0\'s and 1\'s)')
        if len(key) != 64:
            raise DESKeyError('Only 64-bit keys are accepted')
        self.__key = key

    def getInitialKey(self):
        """Get the initial key"""
        return self.__key

    def getKey(self, round=16):
        """Generate the 48-bit keys"""
        keyMatrix = np.array([c for c in self.__key]).take(self.__pc1)
        for i in range(1, round+1):
            if i in [1, 2, 9, 16]:
                keyMatrix = np.vstack((self.__leftShift(keyMatrix[:4], 1), self.__leftShift(keyMatrix[4:], 1)))
            else:
                keyMatrix = np.vstack((self.__leftShift(keyMatrix[:4], 2), self.__leftShift(keyMatrix[4:], 2)))
        return ''.join(keyMatrix.take(self.__pc2).flatten())
    
    def __leftShift(self, matrix, shift):
        """Shift the elements of matrix to the left"""
        indices = range(shift, matrix.size) + range(shift)
        return matrix.flatten().take(indices).reshape(matrix.shape)


if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = DESKey()

    # key = raw_input('Enter a 64-bit key: ')
    # myObj.setInitialKey(key)

    for i in range(1,17):
        print('Round {}: {}'.format(i, myObj.getKey(i)))