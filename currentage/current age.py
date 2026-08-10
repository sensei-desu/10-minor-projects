from datetime import datetime

def calculate_age():
    print("=== Age Calculator ===")
    
    while True:
        date_str = input("\nEnter birth date as YYYY-MM-DD (or 'q' to quit): ").strip()
        
        if date_str.lower() == 'q':
            print("Bye!")
            break

        try:
            birth_date = datetime.strptime(date_str, "%Y-%m-%d")
            today = datetime.now()

            if birth_date > today:
                print("Birth date can't be in the future!")
                continue

            # Calculate exact years and total days
            age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            age_days = (today - birth_date).days

            print(f" You are {age_years} years old ({age_days:,} days total)!")

        except ValueError:
            print("Invalid date! Use format YYYY-MM-DD (e.g., 2000-05-15).")

if __name__ == "__main__":
    try:
        calculate_age()
    except Exception as e:
        print(f"\nScript crashed: {e}")
    finally:
        input("\nPress Enter to exit...")
