
# Define a function for each arithmetic operation
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Main program
print("Basic Calculator")
print("----------------")

# Prompt user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt user to input an operation choice
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
op_choice = int(input("Enter your choice (1/2/3/4): "))

# Perform calculation based on user's choice
if op_choice == 1:
    result = add(num1, num2)
    print(f"Result: {num1} + {num2} = {result}")
elif op_choice == 2:
    result = sub(num1, num2)
    print(f"Result: {num1} - {num2} = {result}")
elif op_choice == 3:
    result = mul(num1, num2)
    print(f"Result: {num1} * {num2} = {result}")
elif op_choice == 4:
    result = div(num1, num2)
    print(f"Result: {num1} / {num2} = {result}")
else:
    print("Invalid operation choice!")
