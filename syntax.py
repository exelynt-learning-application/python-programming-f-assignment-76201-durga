# Program Title
print("=== Python Syntax Structure Demo ===")

# Top-level print statements
print("Welcome to the program.")
print("This program demonstrates indentation.")
print("Python uses indentation to define code blocks.")

number = 10

# Code block starts here.
# Indentation is required in Python to indicate that
# the following statements belong to the if block.
if number > 5:
    print("The number is greater than 5.")

    # Nested block starts here.
    # This block is inside the if statement.
    if number == 10:
        print("The number is exactly 10.")
        print("This is a nested block.")

    # Nested block ends here.

    print("End of the if block.")

# Code block ends here.

print("Program executed successfully.")
