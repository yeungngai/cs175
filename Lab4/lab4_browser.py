#----------------------------------------------------
# Lab 4, Exercise 2: Web browser simulator
# Purpose of code:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack


def getAction():
    '''
    This method prompts user to input a command and return the command. If the command is not valid,
    the method prints out corresponding message.
    '''
    actions = ['=', 'q', '<', '>']
    command = input('Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
    if command not in actions:
        print('Invalid entry.')
    else:
        return command


def goToNewSite(current, bck, fwd):
    '''
    This method prompts user to enter a website and adds the current one to history.
    If user enters a new website in history, the methods also clears the forward history.
    '''

    if bck.isEmpty():
        bck.push(current)
    if bck.items.index(current) < bck.size() - 1:
        del bck.items[bck.items.index(current) + 1: bck.size()]

    newSite = str(input('URL: '))
    current = newSite
    bck.push(current)

    return current


def goBack(current, bck, fwd):
    '''
    This method allows user to go back to the history website before the current one.
    If the very first website is already the current one, the method prints out a warning message.
    '''

    if bck.isEmpty() or current == bck.items[0]:
        print('Cannot go back')
    else:
        current = bck.items[bck.items.index(current) - 1]

    return current


def goForward(current, bck, fwd):
    '''
    This method allows user to go forward if the user is browsing a history website.
    The method prints out a warning message if there is no forward history. 
    '''

    if bck.isEmpty() or current == bck.peek():
        print('Cannot go forward')
    else:
        current = bck.items[bck.items.index(current) + 1]

    return current


def main():
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        action = getAction()
        
        if action == '=':
            current = goToNewSite(current, back, forward)
        elif action == '<':
            current = goBack(current, back, forward)
        elif action == '>':
            current = goForward(current, back, forward)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()


