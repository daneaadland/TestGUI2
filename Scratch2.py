'''Created on Dec 24, 2017, @author: daneaadland'''

from Drink import Drink

#first_name = input("Enter drink name:")
#first_amt = input("Enter drink quantity in ounces:")
#first_abv= input("Enter drink alcohol in ounces:")
first_name = 'Vodka'
first_amt=1
first_abv=0.3

first_drink = Drink(first_name, first_amt, first_abv)

print(first_drink)
print(first_drink.name)
print(first_drink.amt)
print(first_drink.abv)

