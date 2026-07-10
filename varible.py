# Student Profile Program

# Store student details using different data types
student_name = "Akshay Khedkar"   # String
student_age = 23                  # Integer
student_percentage = 85.5         # Float
is_passed = True                  # Boolean

# Display student details
print("=== Student Profile ===")
print("Name:", student_name)
print("Age:", student_age)
print("Percentage:", student_percentage)
print("Passed:", is_passed)

# Type checking using type()
print("\n=== Data Types ===")
print("Type of student_name:", type(student_name))
print("Type of student_age:", type(student_age))
print("Type of student_percentage:", type(student_percentage))
print("Type of is_passed:", type(is_passed))

# Demonstrate dynamic typing
student_age = "Twenty Three"

print("\n=== Dynamic Typing ===")
print("Updated student_age:", student_age)
print("Type of updated student_age:", type(student_age))
