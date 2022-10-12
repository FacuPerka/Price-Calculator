product = input('Write the product name: ')
price = int(input('Write the price: '))
discount = int(input('Enter the discount percentage: '))
finalPrice = price - discount * price / 100

print ('The price of the ' + product + ' is ' + (str(finalPrice)))
