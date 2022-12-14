# Program to show number of characters in a name using type casting

name = input("Enter your name : ")
length = len(name)
type = str(length)
print("Your name has " + type + " characters")

"""
Casting in python is  done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""
