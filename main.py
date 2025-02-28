print("checking Github")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Choose an option: ")
    if choice in ["1", "2", "3", "4"]:

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == "5":
        break

