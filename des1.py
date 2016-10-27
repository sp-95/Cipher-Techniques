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
        """Initialize key and the permutation choices"""
        self.__key = '011110000011001111000011001000001101101001110000'

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


if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = DESKey()

    # key = raw_input('Enter the 48-bit key: ')
    # myObj.setKey(key)