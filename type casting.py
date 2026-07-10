# Type Conversion Program

print("=== Arithmetic Operations Using Type Conversion ===")

# Ask the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert user input into integer and float
int_num = int(num1)
float_num = float(num2)

# Perform arithmetic operations
addition = int_num + float_num
subtraction = int_num - float_num
multiplication = int_num * float_num
division = int_num / float_num

# Display the results
print("\n=== Results ===")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Convert numeric value into a string
string_num = str(int_num)
print("\nString Conversion:")
print("The first number as a string is:", string_num)

# Display data types
print("\n=== Data Types ===")
print("Type of int_num:", type(int_num))
print("Type of float_num:", type(float_num))
print("Type of string_num:", type(string_num))
