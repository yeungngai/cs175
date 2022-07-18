
# Exercise 1

# Create lists, print out the id and its content
numbers = [11, 25, 32, 4, 67, 18, 50, 11, 4, 11]
oddNumbers = []
print('The contents of object ' + str(id(oddNumbers)) + ' are ' + str(oddNumbers))

# A for loop that adds all odd numbers to oddNumber list
for x in numbers:
    if x % 2 == 1:
        oddNumbers.append(x)

# Print out the contents and id of oddNumber
print('The contents of object ' + str(id(oddNumbers)) + ' have been updated to ' + str(oddNumbers))

# Determine the largest and the smallest number in oddNumber
oddNumbers.sort(reverse=True)
minNumber = oddNumbers.pop(len(oddNumbers)-1)
maxNumber = oddNumbers.pop(0)

# Print out the updates in list oddNumber
print('The smallest odd number, ' + str(minNumber) + ', has been removed from the list of odd numbers.')
print('The largest odd number, ' + str(maxNumber) + ', has been removed from the list of odd numbers.')

# Print out the content of oddNumber
print('The contents of object ' + str(id(oddNumbers)) + ' have been updated to ' + str(oddNumbers))
print('There are ' + str(len(numbers)) + ' numbers in the original list.')

# Remove the smallest number and print out the content
for i in numbers:
    if i == minNumber:
        numbers.remove(i)
print('After removing the smallest odd number, there are ' + str(len(numbers)) + ' numbers in the list:' + str(numbers))

