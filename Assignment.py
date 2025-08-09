# Task 1: Perform Basic Mathematical Operations

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1 = int(num1)
num2 = int(num2)
print("choose the operation:")
print("1. Addition(+):")
print("2. subtraction(-):")
print("3. multiplication(*):")
print("4. division(/):")
choice = input("choose (1/2/3/4): ")
if choice == "1":
    Addition = num1 + num2
    print("Addition:", Addition)
if choice == "2":
    Subtraction = num1 - num2
    print("Subtraction:", Subtraction)
if choice == "3":
    Multiplication = num1 * num2
    print("Multiplication:", Multiplication)
if choice == "4":
    Division = num1/num2
    print("Division:", Division)

# Task 2: Create a persionalized greeting

user_name = input("Enter your first name: ")
user_lname = input("Enter your last name: ")
print(f"Hello, {user_name} {user_lname}! Welcome to the python program.")
