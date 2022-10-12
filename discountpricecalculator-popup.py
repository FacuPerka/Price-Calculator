##This code is used to calculate the price of a product based on a discount written by the user. It has a pop-up window with the result.
import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.withdraw()

product = input('Write the product name: ')
price = int(input('Write the product price: '))
discount = int(input('Enter the discount percentage: '))
finalPrice = price - discount * price / 100

messagebox.showinfo("Calculation", 'The price of the ' + product + ' it is ' + (str(finalPrice))) 
