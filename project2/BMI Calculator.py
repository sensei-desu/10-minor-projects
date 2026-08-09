def calculate_bmi():
    print("=== BMI Health Calculator ===")
    
    while True:
        print("\nChoose height unit:")
        print("1. Centimeters (cm)")
        print("2. Feet (ft)")
        print("3. Quit")
        
        unit = input("Select option (1-3): ").strip()
        
        if unit == '3':
            print("Bye!")
            break

        if unit not in ('1', '2'):
            print("Invalid choice, try again.")
            continue

        try:
            weight = float(input("Enter weight (in kg): "))
            
            if unit == '1':
                height_cm = float(input("Enter height (in cm): "))
                height_m = height_cm / 100
            else:
                height_ft = float(input("Enter height (in feet, e.g., 5.75): "))
                height_m = height_ft * 0.3048

            if weight <= 0 or height_m <= 0:
                print("Weight and height must be greater than zero.")
                continue

        except ValueError:
            print("Please enter valid numbers only.")
            continue

        bmi = weight / (height_m ** 2)
        print(f"\nYour BMI is: {bmi:.1f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")

if __name__ == "__main__":
    try:
        calculate_bmi()
    except Exception as e:
        print(f"\ Script crashed: {e}")
    finally:
        input("\nPress Enter to exit...")