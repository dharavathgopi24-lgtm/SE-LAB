
from Addition import add
from Subtraction import subtraction
from multiply import multiply
from divide import divide

while True:
    print("\n--- TEAM CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtraction(a, b)
        elif choice == "3":
            result = multiply(a, b)
        else:
            result = divide(a, b)

        print("Result:", result)

    except ValueError as e:
        print("Error:", e)
