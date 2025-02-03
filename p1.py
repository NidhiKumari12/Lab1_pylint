def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    # Addition of two numbers
    num1 = 10
    num2 = 5
    result_add = add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result_add}")

    # Multiplication of two numbers
    result_multiply = multiply(num1, num2)
    print(f"The product of {num1} and {num2} is: {result_multiply}")

    # Subtraction of two numbers
    result_subtract = subtract(num1, num2)
    print(f"The difference when {num2} is subtracted from {num1} is: {result_subtract}")

    # Division of two numbers
    result_divide = divide(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result_divide}")

    # Check if a number is even or odd
    number = 7
    result_even_odd = check_even_odd(number)
    print(f"The number {number} is {result_even_odd}.")

    # Another example with a different number
    number = 4
    result_even_odd = check_even_odd(number)
    print(f"The number {number} is {result_even_odd}.")

if __name__ == "__main__":
    main()
