"""
Caesar Cipher
=============

Input:
    1. String of characters consisting of lowercase and uppercase characters
    2. Shift key for lowercase characters
    3. Shift key for uppercase characters

Output:
    Encrypted and decrypted strings using Caesar Cipher with the given shift keys
"""

import __future__


__author__ = 'Shashanka Prajapati'


class Caesar:
    def __init__(self):
        """initialize with no keys"""
        self.__k1 = 0
        self.__k2 = 0

    def __encryptLetter(self, c):
        """Encrypt a single letter"""
        if c.islower():
            return chr((ord(c) - ord('a') + self.__k1) % 26 + ord('a'))
        elif c.isupper():
            return chr((ord(c) - ord('A') + self.__k2) % 26 + ord('A'))
        else:
            return c

    def __decryptLetter(self, c):
        """Decrypt a single letter"""
        if c.islower():
            return chr((ord(c) - ord('a') - self.__k1) % 26 + ord('a'))
        elif c.isupper():
            return chr((ord(c) - ord('A') - self.__k2) % 26 + ord('A'))
        else:
            return c

    def encrypt(self, input):
        """Encrypt the input string"""
        return ''.join([self.__encryptLetter(c) for c in input])

    def decrypt(self, input):
        """Decrypt the input string"""
        return ''.join([self.__decryptLetter(c) for c in input])

    def setLowerKey(self, key):
        """Set the key value for lowercase letters"""
        self.__k1 = key

    def getLowerKey(self, key):
        """Get the key value for lowercase letters"""
        return self.__k1

    def setUpperKey(self, key):
        """Set the key value for uppercase letters"""
        self.__k2 = key

    def getUpperKey(self, key):
        """Get the key value for uppercase letters"""
        return self.__k2


if __name__ == '__main__':  # if this file is being executed and not imported
    message = raw_input("Enter your message: ")
    k1 = int(raw_input("Enter key for lowercase characters: "))
    k2 = int(raw_input("Enter key for uppercase characters: "))

    myObj = Caesar()
    myObj.setLowerKey(k1)
    myObj.setUpperKey(k2)

    cipher = myObj.encrypt(message)
    print("Cipher Text: {}".format(cipher))

    plain = myObj.decrypt(cipher)
    print("Plain Text: {}".format(plain))