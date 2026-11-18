
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    try:
        print("Division Result:", divide(num1, num2))
    except ValueError as e:
        print("Error:", e)
