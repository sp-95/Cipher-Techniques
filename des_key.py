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


class DESKey:
    def __init__(self):
        self.__key = '0000111100010101011100011100100101000111110110011110100001011001'

    def setInitialKey(self, key):
        self.__key = key

    def getInitialKey(self):
        return self.__key


if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = DESKey()

    key = raw_input('Enter a 64-bit key: ')
    myObj.setInitialKey(key)