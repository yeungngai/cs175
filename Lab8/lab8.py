#
# CMPUT 175
# Lab 8
#
# First name: Yi
# Last name: Yang
# Lab section: D04
#
# Description: These are the Recursion and Search exercises
#
#

# exercise 1:

def mylen(some_list):
    if some_list == []:
        return 0
    else:
        return 1 + mylen(some_list[1:])


def main():
    alist = [43, 76, 97, 86]
    print(mylen(alist))

main()


# exercise 2:

def intDivision(dividend, divisor):
    if dividend < divisor:
        return 0
    else:
        return 1 + intDivision(dividend - divisor, divisor)


def main():
    try:
        n = int(input('Enter an integer dividend: '))
        m = int(input('Enter an integer divisor: '))
        if n < 0 or m < 0:
            raise ValueError
        if m == 0:
            raise ZeroDivisionError
    except ValueError:
        print("Dividend or divisor is not a positive integer")
    except ZeroDivisionError:
        print("Divisor cannot be zero")
    else:
        print('Integer division', n, '//', m, '=', intDivision(n,m))

main()


# exercise 3:

def sumdigits(n):
    if str(n) == str(n)[len(str(n))-1]:
        return n
    else:
        return int(str(n)[0]) + sumdigits(int(str(n)[1:]))


def main():
    try:
        number = int(input('Enter a number: '))
        if number <= 0:
            raise ValueError
    except ValueError:
        print("Not a positive integer")
    else:
        print(sumdigits(number))

main()


# exercise 4:

def reverseDisplay(n):
    if len(str(n)) == 1:
        return n
    else:
        return str(n)[len(str(n))-1] + str(reverseDisplay(int(str(n)[:len(str(n))-1])))


def main():
    try:
        number = int(input('Enter a number: '))
        if number <= 0:
            raise ValueError
    except ValueError:
        print("Not a positive integer")
    else:
        print(reverseDisplay(number))

main()


# exercise 5:

def binary_search2(key, alist, lowerBound, upperBound):
    if lowerBound <= upperBound:
        guessIndex = (lowerBound + upperBound) // 2
        if key == alist[guessIndex]:
            return guessIndex
        elif key > alist[guessIndex]:
            return binary_search2(key, alist, lowerBound, guessIndex - 1)
        elif key < alist[guessIndex]:
            return binary_search2(key, alist, guessIndex + 1, upperBound)
    else:
        return -1


def main():
    some_list = [9,7,5,3,1,-2,-8]
    print(binary_search2(9,some_list,0,len(some_list)-1))
    print(binary_search2(-8,some_list,0,len(some_list)-1))
    print(binary_search2(4,some_list,0,len(some_list)-1))

main()

