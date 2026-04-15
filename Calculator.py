import sys

# ---------------- CORE FUNCTIONS ---------------- #

def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return None, None


def add():
    a, b = get_numbers()
    if a is not None:
        print(f"Result: {a} + {b} = {a + b}")


def subtract():
    a, b = get_numbers()
    if a is not None:
        print(f"Result: {a} - {b} = {a - b}")


def multiply():
    a, b = get_numbers()
    if a is not None:
        print(f"Result: {a} × {b} = {a * b}")


def divide():
    a, b = get_numbers()
    if a is not None:
        if b == 0:
            print("Error: Division by zero not allowed!")
        else:
            print(f"Result: {a} ÷ {b} = {a / b}")


def power():
    a, b = get_numbers()
    if a is not None:
        print(f"Result: {a} ^ {b} = {a ** b}")


def modulus():
    a, b = get_numbers()
    if a is not None:
        print(f"Result: {a} % {b} = {a % b}")


# ---------------- UI FUNCTIONS ---------------- #

def show_menu():
    print("\n" + "="*40)
    print("ADVANCED PYTHON CALCULATOR")
    print("="*40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    print("="*40)


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        elif choice == "5":
            power()
        elif choice == "6":
            modulus()
        elif choice == "7":
            print("Thank you for using calculator!")
            sys.exit()
        else:
            print("Invalid choice! Try again.")


# ---------------- ENTRY POINT ---------------- #

if __name__ == "__main__":
    main()
