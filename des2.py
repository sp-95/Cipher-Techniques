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
        pass


if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = DES()