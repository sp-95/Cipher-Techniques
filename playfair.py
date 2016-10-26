"""
Playfair Cipher
===============

Input:
    Input string and a key string

Output:
    1. Key matrix based on the key string
    2. Encrypted string using Playfair Cipher with key as the key string
    3. Decrypted string usiing Playfair Cipher with key as the key string
"""

import __future__


__author__ = 'Shashanka Prajapati'


import re               # Regular Expression
import numpy as np      # Handles n-dimentional lists


class Playfair:
    def __init__(self):
        """Initialize class with no key"""
        self.__generateMatrix('')
    
    def __generateMatrix(self, key):
        """Generate a 5x5 matrix based on the given key"""
        matrix = [j for i,j in enumerate(key) if j not in key[:i]]
        self.__matrix = np.array(matrix + [c for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if c not in matrix]).reshape(5,5)     # 'J' isn't included
    
    def __generatePairs(self, input):
        """Split the input into pairs"""
        input = self.__validCharacters(input)
        pairs = []

        counter = 0
        while counter < len(input):
            if counter + 1 == len(input):               # end of input
                pairs.append(input[counter] + 'X')
            elif input[counter] != input[counter + 1]:  # normal pair
                pairs.append(input[counter:counter+2])
                counter += 1
            else:
                pairs.append(input[counter] + 'X')      # padding for double letter pair
            counter += 1

        return pairs
    
    def __encryptPair(self, input):
        """Encrypt a pair using the key matrix"""
        first = self.__getCoordinates(input[0])
        second = self.__getCoordinates(input[1])
        
        if first[0] == second[0]:   # letters are in the same column
            cipher = self.__matrix[first[0], (first[1] + 1) % 5] + self.__matrix[second[0], (second[1] + 1) % 5]
        elif first[1] == second[1]: # letters are in the same row
            cipher = self.__matrix[(first[0] + 1) % 5, first[1]] + self.__matrix[(second[0] + 1) % 5, second[1]]
        else:                       # letters are not in the same row or column, i.e. they form a rectangle
            cipher = self.__matrix[first[0], second[1]] + self.__matrix[second[0], first[1]]
        
        return cipher
    
    def __decryptPair(self, input):
        """Decrypt a pair using the key matrix"""
        first = self.__getCoordinates(input[0])
        second = self.__getCoordinates(input[1])
        
        if first[0] == second[0]:   # letters are in the same column
            cipher = self.__matrix[first[0], (first[1] - 1) % 5] + self.__matrix[second[0], (second[1] - 1) % 5]
        elif first[1] == second[1]: # letters are in the same row
            cipher = self.__matrix[(first[0] - 1) % 5, first[1]] + self.__matrix[(second[0] - 1) % 5, second[1]]
        else:                       # letters are not in the same row or column, i.e. they form a rectangle
            cipher = self.__matrix[first[0], second[1]] + self.__matrix[second[0], first[1]]
        
        return cipher
    
    def encrypt(self, input):
        """Encryption"""
        pairs = self.__generatePairs(input)
        return ''.join([self.__encryptPair(pair) for pair in pairs])
    
    def decrypt(self, input):
        """Decryption"""
        pairs = self.__generatePairs(input)
        return ''.join([self.__decryptPair(pair) for pair in pairs])
    
    def setKey(self, key):
        """Set a key value"""
        key = self.__validCharacters(key)
        self.__generateMatrix(key)

    def getKey(self):
        """Get the key matrix"""
        return self.__matrix

    def __validCharacters(self, input):
        """Strip non-alphabetic characters and the letter 'J' from the input and convert it to uppercase"""
        return re.sub('[^A-Za-z]', '', input).upper().replace('J', 'I')

    def __getCoordinates(self, letter):
        """Get the coordinates of a letter in the key matrix"""
        x, y = np.where(self.__matrix==letter)
        return x[0], y[0]


if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = Playfair()
    
    message = raw_input('Enter your message: ')
    key = raw_input('Enter the key: ')

    myObj.setKey(key)
    print('Key matrix:')
    for row in myObj.getKey():
        print(row)

    cipher = myObj.encrypt(message)
    print('Cipher Text: {}'.format(cipher))

    plain = myObj.decrypt(cipher)
    print('Plain Text: {}'.format(plain))