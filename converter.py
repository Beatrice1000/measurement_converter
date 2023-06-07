# -*- coding: utf-8 -*-


print ("** FOOD MEASUREMENT CONVERTER **\n\n")
start=input("Type START to open converter: ")

while True:
    print("\n\n")
    print("What do you want to convert VOLUME or MASS: Enter 1 if VOLUME and 2 if MASS\n")
    type_of_converter = input("Please enter your choice: ")
    if (type_of_converter =="1"):
        print("You chose a volume converter.")
        print("For Litres to Cups type *litres_to_cups* and for Cups to Litres type *cups_to_litres*")
        option=input("Enter your Volume selection: ")
        if(option=='litres_to_cups'):
            number_of_litres = float(input("Enter the number of litres : "))
            number_of_cups = number_of_litres * 4.22675
            print("The number of CUPS is: ", number_of_cups)
          
        elif(option=='cups_to_litres'):
            number_of_cups = float(input("Enter the number of cups : "))
            number_of_litres = number_of_cups * 0.236588
            print("The number of LITRES is: ", number_of_litres)
            
        else:
            print("Wrong option selected")
            break
      
    elif(type_of_converter== "2"):
        print("You chose a Mass Converter")
        print("For Grams to Pound type *grams_to_pounds* and for Pounds to Grams type *pounds_to_grams* and for Pounds to Ounces type *pounds_to_ounces* and for Ounces to Pounds type *ounces_to_pounds ")
        option=input("Enter your Mass selection: ")
        if(option=='grams_to_pounds'):
            number_of_grams = float(input("Enter the number of grams : "))
            number_of_pounds = number_of_grams * 2.00220462
            print("The number of POUNDS is: ", number_of_pounds)
            
        elif(option=='pounds_to_grams'):
            number_of_pounds = float (input("Enter the number of Pounds : "))
            number_of_grams = number_of_pounds * 453.592
            print("The number of GRAMS is: ", number_of_grams)
            
        elif(option=='pounds_to_ounces'):
            number_of_pounds = float (input("Enter the number of Pounds : "))
            number_of_ounces = number_of_pounds * 16
            print("The number of OUNCES is: ", number_of_ounces)
            
        elif(option=='ounces_to_pounds'):
            number_of_ounces = float (input("Enter the number of Ounces : "))
            number_of_pounds = number_of_ounces * 0.0625
            print("The number of POUNDS is: ", number_of_pounds)
            
        else:
            print("Wrong option selected")
            break
    else:
        print("Invalid Option. Please try again")
print("Thanks for using this converter")
       
   











