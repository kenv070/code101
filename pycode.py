import os

operation = int(input(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

os.system('cls' if os.name == 'nt' else 'clear')

if operation == 1:
    print(num1, "+", num2, "=", num1 + num2)
elif operation == 2:
    print(num1, "-", num2, "=", num1 - num2)
elif operation == 3:
    print(num1, "*", num2, "=", num1 * num2)
elif operation == 4:
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid input")