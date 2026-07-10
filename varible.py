# Student Profile Program

# Store student details in variables
student_name = "Akshay Khedkar"   # String
age = 23                          # Integer
course_fee = 50000.00             # Float
is_enrolled = True                # Boolean

# Print student details
print("===== Student Profile =====")
print("Student Name :", student_name)
print("Age          :", age)
print("Course Fee   :", course_fee)
print("Enrolled     :", is_enrolled)

# Display data types
print("\n===== Data Types =====")
print("student_name:", type(student_name))
print("age         :", type(age))
print("course_fee  :", type(course_fee))
print("is_enrolled :", type(is_enrolled))

# Update variables dynamically
age = age + 1                  # Increment age
is_enrolled = False            # Change enrollment status

# Add 10% tax to course fee
tax = course_fee * 0.10
course_fee = course_fee + tax

# Print updated values
print("\n===== Updated Student Profile =====")
print("Student Name :", student_name)
print("Age          :", age)
print("Course Fee   :", course_fee)
print("Enrolled     :", is_enrolled)

# Display updated data types
print("\n===== Updated Data Types =====")
print("student_name:", type(student_name))
print("age         :", type(age))
print("course_fee  :", type(course_fee))
print("is_enrolled :", type(is_enrolled))
