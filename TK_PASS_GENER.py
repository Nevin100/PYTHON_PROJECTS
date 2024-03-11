import tkinter as tk
import string
import random


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
    #Enable text widget for editing
    result_text.config(state = "normal")        
    #clear previous content
    result_text.delete(index1 = "1.0")
    result_text.insert(tk.END, password)
    result_text.config(state = "disabled")
        
def start():
    password_length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()
    
    generate_password (
    length = password_length,
    lowercase = include_lowercase,
    uppercase = include_uppercase,
    digits = include_digits,
    special_chars = include_special_chars
)     
#main program
#Create the main window..
root = tk.Tk()
root.title("Example")

#Root size
root.geometry("400x300")

#label for entry field..
length_label = tk.Label(root, text="Enter number")
length_label.pack()

#Entry field for user..
length_entry = tk.Entry(root)
length_entry.pack()

#button
button = tk.Button(root, text = "Submit", command = start)
button.pack()

#checkbox
uppercase_var = tk.BooleanVar(value = True)
uppercase = tk.Checkbutton(root, text= "include_uppercase", variable = uppercase_var)
uppercase.pack()  

lowercase_var = tk.BooleanVar(value = True)
lowercase = tk.Checkbutton(root, text= "include_lowercase", variable = lowercase_var)
lowercase.pack()

digits_var = tk.BooleanVar(value = True)
digits = tk.Checkbutton(root, text= "include_digits", variable = digits_var)
digits.pack()

special_chars_var = tk.BooleanVar(value = True)
special_chars = tk.Checkbutton(root, text= "include_special_chars_var", variable = special_chars_var)
special_chars.pack()

#text widget
result_text = tk.Text(root, wrap="word" , height = 5, state = "disabled")
result_text.pack()
root.mainloop()