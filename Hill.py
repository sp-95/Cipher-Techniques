import re               # Regular Expression
import numpy as np      # Handles n-dimentional lists

class HillCipherError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class Hill:
    # Initialize class with key matrix [1]
    def __init__(self):
        self.__size = 1
        self.__key = np.array([1])

    # Set size for key matrix
    def setSize(self, size):
        print('Enter a key matrix of size {}:'.format(size))
        matrix = []
        for _ in range(size):
            row = map(int, raw_input().split())
            if len(row) != size:
                raise HillCipherError('Input should be of size {}'.format(size))
            matrix.append(row)
        self.setKey(matrix)

    # Get size of the key matrix
    def getSize(self):
        return self.__size

    # Set the key matrix
    def setKey(self, matrix):
        matrix = np.array(matrix)

        if not self.__isSquare(matrix):
            raise HillCipherError('The key matrix should be a square matrix')
        if np.linalg.det(matrix) == 0:
            raise HillCipherError('Non-invertible Singular Matrix')

        self.__size = len(matrix)
        self.__key = matrix

    # Get the key matrix
    def getKey(self):
        return self.__key

    # Get Inverse of the key matrix
    # 1. Take regular inverse
    # 2. Find the determinant
    # 3. Multiply and round to integers
    # 4. Multiply by determinant's multiplicative inverse (modulo 26)
    def __getKeyInv(self):
        key = np.around(np.multiply(np.linalg.det(self.__key), np.linalg.inv(self.__key)))
        det = self.__modInv(round(np.linalg.det(self.__key)) % 26, 26)
        return np.mod(np.multiply(det, key), 26)

    # Segment the input according to the matrix size
    def __getSegments(self, input):
        input = self.__validCharacters(input)
        input = input + 'X'*((self.__size - len(input) % self.__size) % self.__size)
        return re.findall('.{{{}}}'.format(self.__size), input)

    # Generate matrix for each segment
    def __generateMatrix(self, segment):
        return np.array([ord(x) - ord('A') for x in segment]).reshape(self.__size, 1)

    # Encrypt each segment
    def __encryptSegment(self, segment):
        cipher = np.mod(np.dot(self.getKey(), self.__generateMatrix(segment)), 26)
        return ''.join([chr(x + ord('A')) for x in cipher])

    # Decrypt each segment
    def __decryptSegment(self, segment):
        plain = np.mod(np.dot(self.__getKeyInv(), self.__generateMatrix(segment)), 26)
        return ''.join([chr(x + ord('A')) for x in plain])

    # Encryption
    def encrypt(self, input):
        segments = self.__getSegments(input)
        return ''.join([self.__encryptSegment(segment) for segment in segments])

    # Decryption
    def decrypt(self, input):
        segments = self.__getSegments(input)
        return ''.join([self.__decryptSegment(segment) for segment in segments])

    # Check if the matrix is a square matrix
    def __isSquare(self, matrix):
        return all([len(row) == len(matrix) for row in matrix])

    # Strip non-alphabetic characters from the input and convert it to uppercase
    def __validCharacters(self, input):
        return re.sub('[^A-Za-z]', '', input).upper()

    # Euclidean GCD
    def __egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.__egcd(b % a, a)
            return g, x - (b // a) * y, y

    # Inverse Modulo
    def __modInv(self, a, m):
        g, x, y = self.__egcd(a, m)
        if g != 1:
            raise HillCipherError('Modular inverse doesn\'t exist')
        else:
            return x % m

if __name__ == '__main__':  # if this file is being executed and not imported
    myObj = Hill()

    message = raw_input('Enter your message: ')
    size = int(raw_input('Enter size for the key matrix: '))
    myObj.setSize(size)

    # myObj.setKey([[0, 11, 15], [7, 0, 1], [4, 19, 0]])
    # print('Key Matrix:')
    # for row in myObj.getKey():
    #     print(row)

    cipher = myObj.encrypt(message)
    print('Cipher Text: {}'.format(cipher))

    plain = myObj.decrypt(cipher)
    print('Plain Text: {}'.format(plain))