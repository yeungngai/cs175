#
# CMPUT 175
# Lab 1
#
# First name: Yi
# Last name: Yang
# Lab section: D04
#
# Description: These are the python warm up exercises
#
#

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


# Exercise 2

# Create a tuple for months
months = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT')
print('The contents of object ' + str(id(months)) + ' are ' + str(months))

# Update the tuple and print out its contents
months = months + ('NOV', 'DEC')
print('The contents of object ' + str(id(months)) + ' are ' + str(months))

# Create a list for precipitation in 2019 and print out its contents
precipitation2019 = [15.5, 12.1, 18.5, 15.6, 10.7, 62.2, 41.4, 58.3, 15.7, 15.3, 24.8]
precipitation2019.insert(6, 67.8)
print(str(precipitation2019[3]) + 'mm fell in ' + months[3] + ' 2019.')

# Prompt user to input a month
inputMonth = str(input('Please enter a month: '))

# Print out the result
if inputMonth in months:
    index = months.index(inputMonth)
    print(str(precipitation2019[index]) + 'mm fell in ' + months[index] + ' 2019.')
else:
    print('The information is not found for the month: ' + inputMonth + '.')


# Exercise 3

# Create a set for animals and print out its contents
animals = {'dog', 'cat', 'fish', 'snake'}
print('The content of object ' + str(id(animals)) + ' are ' + str(animals))

# Update the set and print out its contents
animals.remove('snake')
animals.add('bird')
print('The content of object ' + str(id(animals)) + ' are ' + str(animals))

# Create another list for animals and print out the result
animals2 = {'dog', 'cat', 'rabbit', 'hamster'}
print('Alice would buy ' + str(animals & animals2) + ' from Pets R Us.')


# Exercise 4

# Create dictionaries
bulbs = {'daffodil': 0.35, 'tulip': 0.33, 'crocus': 0.25, 'hyacinth': 0.75, 'bluebell': 0.50}
Mary = {'daffodil': 50, 'tulip': 100}

# Update the dictionary
bulbs['tulip'] = round(bulbs['tulip'] * 1.25, 2)
Mary.update({'hyacinth': 30})

# Print out the results
sortedKeys = sorted(Mary.keys())
print('You have purchased the following bulbs:')

totalBulbs = 0
totalCost = 0
for i in sortedKeys:
    upperKeys = i.upper()
    print(upperKeys[0:3] + ' * %3.0f = $ %4.2f' % (Mary[i], Mary[i] * bulbs[i]))
    totalCost = totalCost + (Mary[i] * bulbs[i])
    totalBulbs = totalBulbs + Mary[i]

print('\nThank you for purchasing %3.0f bulbs from Bluebell Greenhouses.'
      '\nYour total comes to $ %4.2f.' % (totalBulbs, totalCost)
      )

