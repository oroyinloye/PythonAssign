# Ask user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user for operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."

    # Print the result
print("The result is:", result)

print("Thank you for using the calculator program!")


