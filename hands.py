# -----------------------------------------
# My First Python Program
# This program demonstrates variables,
# input/output, type casting, and arithmetic operations.
# -----------------------------------------

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
favorite_number = float(input("Enter your favorite number: "))

# Display user details
print("\n===== User Details =====")
print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")
print("Favorite Number:", favorite_number)

# Display data types
print("\n===== Data Types =====")
print("Type of Name:", type(name))
print("Type of Age:", type(age))
print("Type of Height:", type(height))
print("Type of Favorite Number:", type(favorite_number))

# Perform an arithmetic operation
result = age + favorite_number

# Display the result
print("\n===== Arithmetic Operation =====")
print("The sum of your age and favorite number is:", result)

# End of program
print("\nThank you for using My First Python Program!")
