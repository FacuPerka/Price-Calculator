###Calculate a price with vat and discount
import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.withdraw()

product = input('Write the product name: ')
price = int(input('Write the product price: '))
vat = int(input('Write the VAT percentaje: '))
discount = int(input('Enter the Discount Percentage: '))
finalVAT = (vat * price) / 100
finalDiscount = discount / 100 * price
finalPrice = price + finalVAT - finalDiscount

messagebox.showinfo("Calculation", 'The final price of the ' + product + ' it is ' + (str(finalPrice)))
