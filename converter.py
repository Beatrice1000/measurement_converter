# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("** FOOD MEASUREMENT CONVERTER **\n\n")
print("What do you want to convert VOLUME or MASS: Enter 1 if VOLUME and 2 if MASS\n")
type_of_converter = input("Please enter your choice: ")

if (type_of_converter =="1"):
  print("You chose a volume converter.")
conversion_number =  input()
if (conversion_number == "3"):
   to_value = from_value * 2.11338
  print(f'{from_value} {from_unit} -> {to_value} {to_unit}')
elif(type_of_converter== "2"):
  print("You chose a Mass Converter")
else:
  print("Invalid Option. Please try again")

print ()
conversions_available = [(3, "pounds", "grams"),
                         (4, "grams", "pounds"),
                         (5, "pounds", "ounces"),
                         (6, "cup", "litre"),
                         (7, "litre", "cup")
                        ]
print("conversions available:")
print()

for conversion_number, from_unit, to_unit in conversions_available:
  print(f'{conversion_number}) {from_unit} ->')

print()
conversion = input("Enter the number of the conversion to use --> ")
conversion_index = int(conversion) -1

conversion_number, from_unit, to_unit = conversions_available[conversion_index]
print()
from_value = float(input(f'Enter {from_unit} --> ')) 
print()

