
# Unit Calculator

# go from F to C
# Unit Calculator


# or go from F to K
# or gallons to liltres
#convert to kelvin 

#start by having a list to choose which unit
# input unit
#after unit is chosen print how to convert it
# input Temperature
# answer shown

Title = "Kelvin Calculator"
formula_C = "T(K) = T(°C) + 273.15"
formula_F = "T(K) = (T(°F) + 459.67)× 5/9"
formula_FC = "T(°F) = T(°C) × 1.8 + 32"

print(Title)

unit = input("Enter Celsius or Fahrenheit ")
if unit.lower() == "celsius":
    print(formula_C)
    D = float(input("degree "))
    K_con = D + 273.15
    print(str(D) + " degrees is " + str(K_con) + " Kevlin")
elif unit.lower() == "fahrenheit":
    print(formula_F)
    D = float(input("degree "))
    K_convert = (D + 459.67) * 5/9
    print(str(D) + " degrees is " + str(K_convert) + " Kelvin")
while True:
    cont = input("Would you like to continue?")
    if cont == " yes":
        cont == input("Would you like to convert from Celsius to Fahrenheit")
        cont == " celsius to fahrenheit"
        print(formula_FC)
        D = float(input("degree "))
        FC = D * 1.8 + 32
        print(str(D) + " degrees celsius is " + str(FC) + " fahrenheit")
    elif cont == "no":
        break
    else:
        print("Invalid input")
        













#EXTRA COMMENTS

##    IGNORE
##while True:
##    cont = input("Would you like to continue with different conversions?")
##    if cont.lower == "yes":
##        inpt == input("Choose a conversion: Celsius to Fahrenheit, inches to feet, ot km to miles")
##    if inpt == "celsius to fahrenheit":
##        print(fomula_FC)
##        D = float(input("degree "))
##        F_C = D * 1.8 + 32
##        print(str(D) + " degrees is " + str(F_C) + "fahrenheit")
##    elif:
##        #inches to feet
##        ...
##        ...
##    elif:
##        #km to meters
##    else:
##        cont == "no"
##        break
##print("Good Job")
##
##
##if cont.lower == "yes":
##    
## 
##    ##    
####Specific_heat = input("Would you like to find out...")
####Sp = input("Would you like to know the specific heat?")
####print(Sp)
####if Sp == "yes":
####    ...
####    ...
####    ...
####else:
####    print("Done")
####    
##
###Read Me f
