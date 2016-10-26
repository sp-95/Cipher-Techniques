class Caesar:
    # initialize with no keys
    def __init__(self):
        self.__k1 = 0
        self.__k2 = 0

    # Encrypt a single letter
    def __encryptLetter(self, c):
        if c.islower():
            return chr((ord(c) - ord('a') + self.__k1) % 26 + ord('a'))
        elif c.isupper():
            return chr((ord(c) - ord('A') + self.__k2) % 26 + ord('A'))
        else:
            return c

    # Decrypt a single letter
    def __decryptLetter(self, c):
        if c.islower():
            return chr((ord(c) - ord('a') - self.__k1) % 26 + ord('a'))
        elif c.isupper():
            return chr((ord(c) - ord('A') - self.__k2) % 26 + ord('A'))
        else:
            return c

    # Encrypt the input string
    def encrypt(self, input):
        return ''.join([self.__encryptLetter(c) for c in input])

    # Decrypt the input string
    def decrypt(self, input):
        return ''.join([self.__decryptLetter(c) for c in input])

    # Set the key value for lowercase letters
    def setLowerKey(self, key):
        self.__k1 = key

    # Get the key value for lowercase letters
    def getLowerKey(self, key):
        return self.__k1

    # Set the key value for uppercase letters
    def setUpperKey(self, key):
        self.__k2 = key

    # Get the key value for uppercase letters
    def getUpperKey(self, key):
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