import re               # Regular Expression
import numpy as np      # Handles n-dimentional lists

class Playfair:
    # Initialize class with no key
    def __init__(self):
        self.__generateMatrix('')
    
    # Generate a 5x5 matrix based on the given key
    def __generateMatrix(self, key):
        matrix = [j for i,j in enumerate(key) if j not in key[:i]]
        self.__matrix = np.array(matrix + [c for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if c not in matrix]).reshape(5,5)     # 'J' isn't included
    
    # Split the input into pairs
    def __generatePairs(self, input):
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
    
    # Encrypt a pair using the key matrix
    def __encryptPair(self, input):
        first = self.__getCoordinates(input[0])
        second = self.__getCoordinates(input[1])
        
        if first[0] == second[0]:   # letters are in the same column
            cipher = self.__matrix[first[0], (first[1] + 1) % 5] + self.__matrix[second[0], (second[1] + 1) % 5]
        elif first[1] == second[1]: # letters are in the same row
            cipher = self.__matrix[(first[0] + 1) % 5, first[1]] + self.__matrix[(second[0] + 1) % 5, second[1]]
        else:                       # letters are not in the same row or column, i.e. they form a rectangle
            cipher = self.__matrix[first[0], second[1]] + self.__matrix[second[0], first[1]]
        
        return cipher
    
    # Decrypt a pair using the key matrix
    def __decryptPair(self, input):
        first = self.__getCoordinates(input[0])
        second = self.__getCoordinates(input[1])
        
        if first[0] == second[0]:   # letters are in the same column
            cipher = self.__matrix[first[0], (first[1] - 1) % 5] + self.__matrix[second[0], (second[1] - 1) % 5]
        elif first[1] == second[1]: # letters are in the same row
            cipher = self.__matrix[(first[0] - 1) % 5, first[1]] + self.__matrix[(second[0] - 1) % 5, second[1]]
        else:                       # letters are not in the same row or column, i.e. they form a rectangle
            cipher = self.__matrix[first[0], second[1]] + self.__matrix[second[0], first[1]]
        
        return cipher
    
    # Encryption
    def encrypt(self, input):
        pairs = self.__generatePairs(input)
        return ''.join([self.__encryptPair(pair) for pair in pairs])
    
    # Decryption
    def decrypt(self, input):
        pairs = self.__generatePairs(input)
        return ''.join([self.__decryptPair(pair) for pair in pairs])
    
    # Set a key value
    def setKey(self, key):
        key = self.__validCharacters(key)
        self.__generateMatrix(key)

    # Get the key matrix
    def getKey(self):
        return self.__matrix

    # Strip non-alphabetic characters and the letter 'J' from the input and convert it to uppercase
    def __validCharacters(self, input):
        return re.sub('[^A-Za-z]', '', input).upper().replace('J', 'I')

    # Get the coordinates of a letter in the key matrix
    def __getCoordinates(self, letter):
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