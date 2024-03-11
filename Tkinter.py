import tkinter as tk

def get_text(text, on=False):
    if on:
        #Enable text widget for editing
        result_text.config(state = "normal")
        #clear previous content
        result_text.delete(index1 = "1.0")
        result_text.insert(tk.END, text)
        result_text.config(state = "disabled")
        
def start():
    text = length_entry.get()
    on = checkbox_var.get()
    
    get_text(text, on)

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
checkbox_var = tk.BooleanVar(value = True)
checkbox = tk.Checkbutton(root, text= "true or false", variable = checkbox_var, command = get_text )
checkbox.pack()  

#text widget
result_text = tk.Text(root, wrap="word" , height = 5, state = "disabled")
result_text.pack()
root.mainloop()