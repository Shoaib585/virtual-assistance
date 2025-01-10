# Arithmetic operations as functions

# Addition
def add(a, b):
    return a + b

# Subtraction
def div(a, b):
    return a - b

# Multiplication
def mul(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Floor Division
def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a // b

# Modulus
def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a % b

# Exponentiation
def exponentiate(a, b):
    return a ** b