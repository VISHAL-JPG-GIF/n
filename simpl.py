# simple_calculator.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print("1. Add")
print("2. Subtract")

choice = input("Enter choice: ")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == "1":
    print("Result:", add(a, b))
elif choice == "2":
    print("Result:", sub(a, b))
else:
    print("Invalid choice")
