import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_specials):
    # Collect all possible characters based on user choices
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    # Ensure at least one type of character is selected
    if not characters:
        return "You need to select at least one type of character!"

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Friendly user interface in the terminal
print("Welcome to the Password Generator!")

try:
    length = int(input("Enter the desired password length (e.g., 12): "))
    use_uppercase = input("Include UPPERCASE letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_specials = input("Include special characters (like !@#)? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_specials)
    print("\nHere is your generated password:")
    print(password)

except ValueError:
    print("Please enter a valid number for password length.")
