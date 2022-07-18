#
# CMPUT 175
# Lab 2
#
# First name: Yi
# Last name: Yang
# Lab section: D04
#
# Description: This program prompts user to input a filename and decrypts the file message
#
#

def getInputFile():
    """This function compares a input filename with the correct filename. The function returns the correct
    filename if input filename matches the correct one, otherwise, the function prompts user to input again"""

    loop = True
    inputFilename = str(input('Enter the input filename:'))
    while loop:
        if len(inputFilename) > 3:
            counter = len(inputFilename) - 1
            extension = ''
            while counter > len(inputFilename) - 4:
                extension = extension + inputFilename[counter]
                counter = counter - 1
            if extension == 'txt':
                loop = False
            else:
                inputFilename = str(input('Invalid file extension. Please re-enter the input filename:'))
        else:
            inputFilename = str(input('Invalid file extension. Please re-enter the input filename:'))

    return inputFilename


def decryption(key, encryptedMessage):
    """This function decrypts the message and prints it out"""

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decryptedMessage = ''
    encryptedMessage = encryptedMessage.lower()

    stripSpace1 = True
    while stripSpace1:
        if encryptedMessage[0] == ' ':
            encryptedMessage = encryptedMessage[1::]
        else:
            stripSpace1 = False
    stripSpace2 = True
    while stripSpace2:
        if encryptedMessage[(len(encryptedMessage)-1)] == ' ':
            encryptedMessage = encryptedMessage[:-1:]
        else:
            stripSpace2 = False

    for i in encryptedMessage:
        if i != ' ':
            epos = alphabet.index(i)
            dpos = epos - key
            decryptedMessage = decryptedMessage + alphabet[dpos]
        else:
            decryptedMessage = decryptedMessage + ' '

    print('The decrypted message is:\n' + decryptedMessage)

    return


def main():
    """This is the main function"""

    filename = getInputFile()
    file = open(filename, 'r')
    fileInList = file.read().splitlines()
    key = int(fileInList[0])
    encryptedMessage = fileInList[1]
    decryption(key, encryptedMessage)


main()

