"""
Made by   : Rohit Kumar Yadav
Created On: 01 Oct 2023
"""
# Program to make a Python pasword Generator Program

import random  # Generate random integers,stings,floats
import string  #The string module is a built-in Python module that provides
                #various string-related constants, functions, and classes
from tkinter import messagebox   # to give messagebox functionality
import tkinter as tk
from tkinter import ttk  #  The ttk module provides a set of themed widgets that have a more modern and consistent look
import pyperclip   #pip install pyperclip  : used for copy and paste clipboard functionality


try: 
    def generate_password():
        length = int(length_entry.get())
        chars = string.ascii_letters # this function return all the characters from(a-z)lower and upper case both
        nums = string.digits         # this function return digits i.e(1234567890)
        symbols = string.punctuation # this function return all the possible symbols i.e(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
        combination = chars + nums + symbols  # combine all the possible combinations
        password = ""
        
        for main in range(length):
            password += "".join(random.choice(combination))

        output_label.config(text="Your Password: %s" % password)
        copy_button.config(state="normal")  # Enable the copy button

    def copy_password():
        password = output_label.cget("text").split(": ")[1]
        pyperclip.copy(password)

    # main window
    main = tk.Tk()
    main.title("Python Password Generator")

    # Adding style and theme
    style = ttk.Style()
    style.theme_use("vista")  

    # Adding the length label and entry
    length_label = ttk.Label(main, text="Password Length:")
    length_label.pack()
    main.iconbitmap('pwg.ico')
    main.geometry("330x140")
    length_entry = ttk.Entry(main)
    length_entry.pack()

    # Adding the generate button
    generate_button = ttk.Button(main, text="Generate", command=generate_password)
    generate_button.pack()

    # Adding the output label
    output_label = ttk.Label(main, text="Output Password:")
    output_label.pack()

    # Adding the copy button
    copy_button = ttk.Button(main, text="Copy", command=copy_password, state="disabled")
    copy_button.pack()

    # Start the main loops
    main.mainloop()

except Exception as e: 
    print(e)
