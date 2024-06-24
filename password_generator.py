import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    length = length_entry.get()
    try:
        length = int(length)
        if length < 8 or length > 16:
            messagebox.showerror("Alert", "Password length should be between 8 and 16 characters.")
        else:
            pass_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                          'h', 'i', 'j', 'k', 'l', 'm', 'n',
                          'o', 'p', 'q', 'r', 's', 't', 'u',
                          'v', 'w', 'x', 'y', 'z', 'A', 'B',
                          'C', 'D', 'E', 'F', 'G', 'H', 'I',
                          'J', 'K', 'L', 'M', 'N', 'O', 'P',
                          'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                          'X', 'Y', 'Z', '1', '2', '3', '4',
                          '5', '6', '7', '8', '9', '0', '!',
                          '@', '#', '$', '%', '^', '&', '*',
                          '(', ')', '?', '<', '>', '/', '|']
            password = "".join(random.choices(pass_chars, k=length))
            password_entry.config(state='normal')
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)
            password_entry.config(state='readonly')
    except ValueError:
        messagebox.showerror("Alert", "Please enter a valid integer for password length.")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard.")
    else:
        messagebox.showerror("Alert", "No password generated.")

window = tk.Tk()
window.title("Random Password Generator")

window.geometry("400x300")
window.resizable(False, False)  

frame = tk.Frame(window)
frame.pack(pady=20)

length_label = tk.Label(frame, text="Enter password length:")
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(frame, width=20)
length_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

password_label = tk.Label(frame, text="Generated Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

password_entry = tk.Entry(frame, width=30, state="readonly")
password_entry.grid(row=2, column=1, padx=10, pady=5)

copy_button = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()