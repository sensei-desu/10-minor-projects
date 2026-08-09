#CALCULATOR
def calculator():
    while True:
        print("\n--- CALCULATOR ---")
        print("1. Add  2. Subtract  3. Multiply  4. Divide  5. Quit")
        choice = input("Pick an option (1-5): ").strip()

        if choice == '5':
            print("Bye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid pick, try again.")
            continue

        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Numbers only, please.")
            continue

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Can't divide by zero!")
            else:
                print(f"Result: {num1 / num2}")

if __name__ == "__main__":
    calculator()