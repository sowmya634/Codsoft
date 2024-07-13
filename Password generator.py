import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return
        
        # Define a pool of characters to choose from
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate a password by selecting random characters from the pool
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password using a messagebox
        messagebox.showinfo("Generated Password", f"Your generated password:\n\n{password}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=30)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Run the main event loop
root.mainloop()
