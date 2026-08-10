import random
import string

def generate_password():
    print("=== Password Generator ===")
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    
    while True:
        user_input = input("\nEnter password length (or 'q' to quit): ").strip()
        
        if user_input.lower() == 'q':
            print("Bye!")
            break
            
        try:
            length = int(user_input)
            if length <= 0:
                print("Length must be greater than 0!")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        password = "".join(random.choice(chars) for _ in range(length))
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    generate_password()
