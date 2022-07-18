
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
