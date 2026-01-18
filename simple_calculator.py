def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y
print("---------------------------------")
print("         Simple Calculator       ")
print("---------------------------------")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Select choice (1/2/3/4): ")

# Check if choice is one of the four options
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '3':
        print(f"{num1} x {num2} = {multiply(num1, num2)}")

    elif choice == '4':
        # The divide function handles the zero check
        result = divide(num1, num2)
        if result == "Error! Division by zero is not allowed.":
            print(result)
        else:
            print(f"{num1} ÷ {num2} = {result}")
else:
    print("Invalid Input")