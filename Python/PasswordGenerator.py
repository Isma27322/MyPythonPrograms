import random
import string
#import pyperclip
#import os

def generate_password():
    # Get user input for minimum requirements
    min_lowercase = int(input("Enter the minimum number of lowercase letters: "))
    min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
    min_digits = int(input("Enter the minimum number of digits: "))
    min_special_chars = int(input("Enter the minimum number of special characters: "))

    # Get user input for password length within valid range (5 to 300)
    while True:
        length = int(input("Enter the password length (between 5 and 200000): "))
        if 5 <= length <= 200000:
            break
        else:
            print("Please enter a valid length.")

    # Ensure the minimum requirements do not exceed the password length
    total_min = min_lowercase + min_uppercase + min_digits + min_special_chars
    while total_min > length:
        print("The sum of minimum requirements exceeds the password length.")
        min_lowercase = int(input("Enter the minimum number of lowercase letters: "))
        min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
        min_digits = int(input("Enter the minimum number of digits: "))
        min_special_chars = int(input("Enter the minimum number of special characters: "))
        total_min = min_lowercase + min_uppercase + min_digits + min_special_chars

    # Generate the password
    lowercase = ''.join(random.choices(string.ascii_lowercase, k=min_lowercase))
    uppercase = ''.join(random.choices(string.ascii_uppercase, k=min_uppercase))
    digits = ''.join(random.choices(string.digits, k=min_digits))
    special_chars = ''.join(random.choices(string.punctuation, k=min_special_chars))

    # Ensure the total length is equal to the user-defined length
    password = lowercase + uppercase + digits + special_chars
    password += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - len(password)))

    # Shuffle the password components
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Copy the password to the clipboard
    #pyperclip.copy(password)
    print (f"The password is now saved to .\passwords\password.pasword")

    #print(f"Generated Password: {password}")
    #print("Password has been copied to the clipboard.")
    with open(".\\paswords\\password.pasword", "w") as passw:
        passw.write(password)
    

if __name__ == "__main__":
    generate_password()
