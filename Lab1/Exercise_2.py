
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

