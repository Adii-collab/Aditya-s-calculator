# type conversion means converting one data type to another data type
# conversion means changing the value of a variable from one data type to another data type automatically
# casting means changing the value of a variable from one data type to another data type manually
#example of conversion
a = 2
b = 3.5
sum = a+b
print(sum) # here a is an integer and b is a float but when we add them the result is a float because of conversion.
#example of casting
a = 2
b = 3.5
sum = a+int(b) # here we are converting b from float to integer using int() function and then adding it to a.
print(sum) # here the result is an integer because we have casted b to an integer before adding it to a.                                            
# to take input from the user we use input() function and it always returns a string so we need to convert it to the desired data type using casting.
name = input("enter your name:")
print ("welcome", name)