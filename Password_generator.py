import random
import string

def generate_password(length=12,uppercase=True,lowercase=True,digits=True,special_chars=True):
    characters=''
    if uppercase:
        characters += string.ascii_uppercase
    
    if lowercase:
        characters += string.ascii_lowercase
        
    if digits:
        characters += string.digits
        
    if special_chars:
        characters += string.punctuation
        
    if not characters:
        print("Error: At least one character type must be selected")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to our password generator")
print("\n")
print("Customize your password by selecting the character types to include")

password_length=int(input("Enter the length of the password "))
include_lowercase = input(" include lowercase letters(y/n)??").lower() == 'y'     
include_uppercase = input(" include uppercase letters(y/n)??").lower() == 'y'     
include_digits = input(" include digits (y/n)??").lower() == 'y'     
include_special_char = input(" include special characters(y/n)??").lower() == 'y'

generated_password = generate_password(
    length = password_length,
    lowercase = include_lowercase,
    uppercase = include_uppercase,
    digits = include_digits,
    special_chars = include_special_char
)     
if generated_password:
    print("Generated password:", generated_password)
    
else:
    print("Sorry nothing generated.. please try again")
     