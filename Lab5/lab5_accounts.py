# ----------------------------------------------------
# Lab 5, Exercise 2: Exceptions and inheritance
# Purpose of code: This program prompts user to enter an account name and performs transactions to the
# corresponding account. The program displays error messages if an incorrect command is input.
#
#
# Author: Yi Yang
# Collaborators/references: None
# ----------------------------------------------------


def processAccounts(accountDic):
    '''
    Prompts user to enter a command, either the account name or to stop the function. The function also checks whether
    or not the correct command is input, if not, an error message is displayed. The function then perform transaction
    to the corresponding account
    '''

    quit = False

    while not quit:
        command = input("Enter account name, or 'Stop' to exit: ")
        if command == 'Stop':
            print('Exiting program...goodbye.')
            quit = True
        else:
            try:
                amount = accountDic[command]
            except KeyError:
                print('Warning! Account for ' + command + ' does not exist. Transaction cancelled')
            else:
                transaction = input('Enter transaction amount for ' + command + ': ')
                try:
                    transaction = float(transaction)
                except ValueError:
                    print('Warning! Incorrect amount. Transaction cancelled')
                else:
                    accountDic[command] = amount + transaction
                    print('New balance for account ' + command + ': ' + str(accountDic[command]))


def readAccounts(inFile):
    '''
    The function takes in the contents of an account file and checks for errors. The function prints out error message,
    returns clients' name and amount as a dictionary.
    '''

    inFileList = []
    for line in inFile:
        line = line.split('>')
        inFileList.append(line)

    accountDic = {}
    for i in inFileList:
        i[1] = i[1].strip()
        try:
            i[1] = float(i[1])
        except ValueError:
            print('Warning! Account for ' + i[0] + ' not added: illegal value for balance')
        else:
            accountDic[i[0]] = i[1]

    inFile.close()

    return accountDic


def main():
    '''
    Prompts user to enter a filename. If an incorrect name is entered, an error message will be printed, otherwise
    this main function passes the content of the entered account file to readAccounts function and calls the
    processAccounts function.
    '''

    fileName = input('Enter filename > ')

    try:
        inFile = open(fileName, 'r')
    except OSError:
        print('File error: ' + fileName + ' does not exist\nExiting program...goodbye.')
    else:
        accountDic = readAccounts(inFile)
        processAccounts(accountDic)


if __name__ == '__main__':
    main()


