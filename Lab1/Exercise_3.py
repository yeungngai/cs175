
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

