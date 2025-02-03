"""This module performs basic arithmetic operations and checks if a number is even or odd."""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def divide(a, b):
    """Divide a by b, returns a message if dividing by zero."""
    if b != 0:
        return a / b
    return "Cannot divide by zero"  # Removed the unnecessary else block

def check_even_odd(number):
    """Check if a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"  # Removed the unnecessary else block

def main():
    """Main function to demonstrate arithmetic operations."""
    num1 = 10
    num2 = 5
    result_add = add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result_add}")

    result_multiply = multiply(num1, num2)
    print(f"The product of {num1} and {num2} is: {result_multiply}")

    result_subtract = subtract(num1, num2)
    print(f"The difference when {num2} is subtracted from {num1} is: {result_subtract}")

    result_divide = divide(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result_divide}")

    number = 7
    result_even_odd = check_even_odd(number)
    print(f"The number {number} is {result_even_odd}.")

    number = 4
    result_even_odd = check_even_odd(number)
    print(f"The number {number} is {result_even_odd}.")

if __name__ == "__main__":
    main()
