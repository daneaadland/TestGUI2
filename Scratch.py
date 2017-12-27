'''Created on Dec 22, 2017@author: daneaadland'''


from Drink import Drink
from Calculator import *

class Drink_Array:

    @classmethod
    def create_array(cls):
        drink_array = []
        return drink_array
    
    def add_drink(self, name, amt, abv):
        test_drink = Drink(name, amt, abv)
        self.__class__.drink_array.append(test_drink)
        self.parse_array(self.__class__.drink_array)
        print(calc_total_amt(self.__class__.drink_array))

    @classmethod
    def parse_array(cls):
        for drk in Drink_Array.drink_array:
            print(drk.name + ', ' + str(drk.amt) + ', ' + str(drk.abv))

d = Drink_Array
testarray = d.create_array()
d.add_drink('Vodka', 1, 0.3)
d.add_drink('Lemonade', 12, 0)
print(Drink_Array.parse_array())

    
#print(calc_total_alcohol())



    