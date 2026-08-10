def is_palindrome():
    print("=== Palindrome Checker ===")
    
    while True:
        word = input("\nEnter a word/phrase (or 'q' to quit): ").strip()
        
        if word.lower() == 'q':
            print("Bye!")
            break

        if not word:
            continue

        cleaned = "".join(char.lower() for char in word if char.isalnum())
        
        if cleaned == cleaned[::-1]:
            print(f"{word}' IS a palindrome!")
        else:
            print(f"{word}' is NOT a palindrome.")

if __name__ == "__main__":
    is_palindrome()
