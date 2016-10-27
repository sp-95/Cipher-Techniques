"""
DES Part 2
==========

Input:
    48-bit input to S-box and 32-bit L

Output:
    32-bit R
"""

import __future__


__author__ = 'Shashanka Prajapati'


import re
import numpy as np


class DESError(Exception):
    """Exception class for DES Algorithm"""
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


class DES:
    def __init__(self):
        self.__input = '111001111010010001100011001111110101101000101110'
        self.__l = '01011010000000000101101000000000'
        self.__sBox = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            ]
        self.__p = [
            15,6,19,20,28,12,27,16,
            0,14,22,25,4,17,30,9,
            1,7,23,13,31,26,2,8,
            18,12,29,5,21,10,3,24,
            ]

    def setInput(self, input):
        if re.search('[^01]', input):
            raise DESError('Input to S-box should contain only bits(0\'s and 1\'s)')
        if len(input) != 48:
            raise DESError('Only 48-bit inputs are accepted')
        self.__input = input

    def setLValue(self, input):
        if re.search('[^01]', input):
            raise DESError('Input to S-box should contain only bits(0\'s and 1\'s)')
        if len(input) != 32:
            raise DESError('Only 32-bit inputs are accepted')
        self.__l = input


if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = DES()

    # input = raw_input('Enter 48-bit input for S-box: ')
    # myObj.setInput(input)
    # l = raw_input('Enter the 32-bit l-value: ')
    # myObj.setLValue(l)