from tkinter import*
import sqlite3

root=Tk()
root.title('Databases')
root.geometry('600x400')

# Databases

# create a database or connect to one
connection = sqlite3.connect('address_book.db') #creates a database file in the same directory if our file doesn't exist.

# create cursor
cursor = connection.cursor()

# create table
cursor.execute("""CREATE TABLE addresses(
               first_name text,
               last_name text,
               address text, 
               city text,
               state text,
               pincode integer
               )""")




# commit changes
connection.commit()

# close connection
connection.close()

root.mainloop()