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
        self.__key = '0000111100010101011100011100100101000111110110011110100001011001'

    def setInitialKey(self, key):
        if re.search('[^01]', key):
            raise DESKeyError('Key should contain only bits(0\'s and 1\'s)')
        if len(key) != 64:
            raise DESKeyError('Only 64-bit keys are accepted')
        self.__key = key

    def getInitialKey(self):
        return self.__key

    def getKey(self, round=16):
        keyMatrix = self.__toMatrix(self.__key)[:,:-1]
        for i in range(1, round+1):
            if i in [1, 2, 9, 16]:
                keyMatrix = np.vstack(self.__leftShift(keyMatrix[:5], 1), self.__leftShift(keyMatrix[5:], 1))
            else:
                keyMatrix = np.vstack(self.__leftShift(keyMatrix[:5], 2), self.__leftShift(keyMatrix[5:], 2))

    def __toMatrix(self, string):
        return np.array([c for c in string]).reshape(8, 8)
    
    def __leftShift(self, matrix, shift):
        indices = range(shift, matrix.size) + range(shift)
        return matrix.flatten().take(indices).reshape(matrix.shape)



if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = DESKey()

    # key = raw_input('Enter a 64-bit key: ')
    # myObj.setInitialKey(key)

    for i in range(1,17):
        print('Round {}: {}'.format(i, myObj.getKey(i)))