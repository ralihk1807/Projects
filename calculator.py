
# pyinstaller file_name.py --onefile -w use this command to convert .py to ,exe file.

import tkinter as tk
from tkinter import *

root  = tk.Tk()
root.title('Calculator')
root.iconbitmap(r'D:\Tut\learn_Tkinter\icons and images\Calculator_30001.ico')
root.configure(bg = '#4d4d4d')

# This is where user enters numbers and commands
entry = tk.Entry(root,width=21, borderwidth=7,font='10', bg='lightgrey', insertbackground='lightgrey')

def update_entry(new_value):
    entry.config(state='normal')
    entry.delete(0, END)
    entry.insert(0, new_value)
    entry.config(state='readonly')

#function for click on a button:
def button_click(character):
    entry.insert(END, character)

#function to clear screen:
def clearscreen():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)
    entry.delete(0, END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    global s_num
    global result

    s_num = float(second_number)
    entry.delete(0, END)

    # Initialize result as None to avoid name error.
    result = None

    if math == 'addition':
        result = f_num + s_num
    elif math == 'subtraction':
        result = f_num - s_num
    # Check for zero division error
    elif math=='division':
        if f_num == 0 or s_num == 0:
            entry.insert(0, 'ERROR')
        else:
            result = f_num / s_num
    elif math == 'multiplication':
        result = f_num * s_num

    # Check if the result is an integer or float.
    if result.is_integer():
        entry.insert(0, str(int(result))) # Display as integer.
    else:
        entry.insert(0, str(result)) # Display as float.

def back_space():
    entry.delete(len(entry.get())- 1, END)


#creating the buttons:
# Buttons with number:
button_9 = tk.Button(root, text='9',padx=30, pady=10, command=lambda: button_click(9),font='3', bg = '#4d4d4d',
                     fg='white')
button_8 = tk.Button(root, text='8',padx=30, pady=10, command=lambda: button_click(8),font='3', bg = '#4d4d4d',
                     fg='white')
button_7 = tk.Button(root, text='7',padx=30, pady=10, command=lambda: button_click(7),font='3', bg = '#4d4d4d',
                     fg='white')

button_6 = tk.Button(root, text='6',padx=30, pady=10, command=lambda: button_click(6),font='3', bg = '#4d4d4d',
                     fg='white')
button_5 = tk.Button(root, text='5',padx=30, pady=10, command=lambda: button_click(5),font='3', bg = '#4d4d4d',
                     fg='white')
button_4 = tk.Button(root, text='4',padx=30, pady=10, command=lambda: button_click(4),font='3', bg = '#4d4d4d',
                     fg='white')

button_3 = tk.Button(root, text='3',padx=30, pady=10, command=lambda: button_click(3),font='3', bg = '#4d4d4d',
                     fg='white')
button_2 = tk.Button(root, text='2',padx=30, pady=10, command=lambda: button_click(2),font='3', bg = '#4d4d4d',
                     fg='white')
button_1 = tk.Button(root, text='1',padx=30, pady=10, command=lambda: button_click(1),font='3', bg = '#4d4d4d',
                     fg='white')

button_0 = tk.Button(root, text='0',padx=30, pady=10, command=lambda: button_click(0),font='3', bg = '#4d4d4d',
                     fg='white')


# Buttons with operations:
button_clear = tk.Button(root, text='C',padx=30, pady=10, command=clearscreen,font='3', bg = '#4d4d4d', fg='white')
button_add = tk.Button(root, text='+',padx=33, pady=10, command=button_add,font='3', bg = '#4d4d4d', fg='white')
button_subtract = tk.Button(root, text='-',padx=36, pady=10, command=button_subtract,font='3', bg = '#4d4d4d',
                            fg='white')
button_divide = tk.Button(root, text='÷',padx=34, pady=10, command=button_divide,font='3', bg = '#4d4d4d',
                          fg='white')
button_multiply = tk.Button(root, text='x',padx=35, pady=10, command=button_multiply,font='3', bg = '#4d4d4d',
                            fg='white')
button_equals = tk.Button(root, text='=',padx=33, pady=10, command=button_equal, bg='#85e0c9', font='3')
button_backspace= tk.Button(root, text='❎',padx=22, pady=10, command=back_space,font='3', bg = '#4d4d4d', fg='white')
button_decimal = tk.Button(root, text='.',padx=36, pady=10, command=lambda: button_click('.'),font='3', bg = '#4d4d4d',
                           fg='white')

#placing widgets on screen
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=30, ipady=20)

button_9.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_7.grid(row=2, column=0)

button_6.grid(row=2, column=1)
button_5.grid(row=3, column=0)
button_4.grid(row=3, column=1)

button_3.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_1.grid(row=5, column=0)

button_0.grid(row=5, column=1)

button_add.grid(row=1, column=2)
button_multiply.grid(row=2, column=2)
button_divide.grid(row=3, column=2)
button_subtract.grid(row=4, column=2)
button_equals.grid(row=5, column=2)
button_clear.grid(row=6, column=0)
button_backspace.grid(row=6, column=1)
button_decimal.grid(row=6, column=2)



root.mainloop()