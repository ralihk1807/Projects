from tkinter import*
import sqlite3
from tkinter import messagebox

root= Tk()
root.title("Database App")
root.geometry('360x500')

# Connect to a database
connection  = sqlite3.connect('address_book.db')

# create a cursor
cursor = connection.cursor()

# create submit function for submit button
def submit():
    # Connect to a database
    connection = sqlite3.connect('address_book.db')

    # create a cursor
    cursor = connection.cursor()

    # Insert into table
    if f_name.get() == '':
        response = messagebox.showerror(title='Empty Field', message='Please fill First Name')
    elif l_name.get() == '':
        response = messagebox.showerror(title='Empty Field', message='Please fill Last Name')
    elif address.get() == '':
        response = messagebox.showerror(title='Empty Field', message='Please fill Address')
    elif city.get() == '':
        response = messagebox.showerror(title='Empty Field', message='Please fill City')
    elif state.get() == '':
        response = messagebox.showerror(title='Empty Field', message='Please fill State')
    elif pincode.get() == '':
        response = messagebox.showerror(title='Empty Field', message='Please fill Pincode')
    else:
        cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :pincode)",
                           {
                                       'f_name':f_name.get(),
                                       'l_name':l_name.get(),
                                       'address':address.get(),
                                       'city':city.get(),
                                       'state':state.get(),
                                       'pincode':pincode.get()
                                      }
                           )
        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        pincode.delete(0, END)

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()





# Create a query function
def query():
    # Connect to a database
    connection = sqlite3.connect('address_book.db')

    # create a cursor
    cursor = connection.cursor()

    # select all the data in the table which we named addresses
    cursor.execute("SELECT *, oid FROM addresses")

    # fetch and save all the table data in a variable as a list of tuples.
    records = cursor.fetchall() # we can also use fetchone() and fetchmany()

    # Loop through results
    print_records = ''

    # format the string and print the result when query button is pressed.
    for record in records:

        print_records += str(record[6])+ " " + str(record[0]) + " " + str(record[1])  + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    # Commit changes
    connection.commit()

    # Close connection
    connection.close()

def delete():
    # Connect to a database
    connection = sqlite3.connect('address_book.db')

    # create a cursor
    cursor = connection.cursor()
    if delete_box.get() == '':
        response = messagebox.showerror(title='Empty Field', message='Please fill ID')
    else:
        cursor.execute("DELETE from addresses WHERE oid=" + delete_box.get())

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()

def update():
    # Connect to a database
    connection = sqlite3.connect('address_book.db')

    # create a cursor
    cursor = connection.cursor()

    record_id = delete_box.get()
    # To update table
    cursor.execute("""UPDATE addresses SET
                      first_name = :first,
                      last_name = :last,
                      address = :address, 
                      city = :city,
                      state = :state,
                      pincode = :pincode
                      
                      WHERE oid = :oid""",

        {'first' : f_name_editor.get(),
                     'last' : l_name_editor.get(),
                     'address' : address_editor.get(),
                     'city' : city_editor.get(),
                     'state' : state_editor.get(),
                     'pincode' : pincode_editor.get(),

                     'oid' : record_id
                   })



    # Commit changes
    connection.commit()

    # Close connection
    connection.close()

    editor.destroy()



def edit():
    global editor
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global pincode_editor


    if delete_box.get() == '':
        response = messagebox.showerror(title='Empty Field', message='Please fill ID')
    else:
        editor = Tk()
        editor.title("Update Record")
        editor.geometry('360x250')

        # Connect to a database
        connection = sqlite3.connect('address_book.db')

        # create a cursor
        cursor = connection.cursor()

        record_id = delete_box.get()

        # select all the data in the table which we named addresses
        cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)

        # fetch and save all the table data in a variable as a list of tuples.
        records = cursor.fetchall()


        #  Create Text entry fields
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))
        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1 )
        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1)
        city_editor = Entry(editor, width=30)
        city_editor.grid(row=3, column=1)
        state_editor = Entry(editor, width=30)
        state_editor.grid(row=4, column=1)
        pincode_editor = Entry(editor, width=30)
        pincode_editor.grid(row=5, column=1)


    # Create text entry labels
        f_name_label = Label(editor, text='First Name')
        f_name_label.grid(row=0, column=0, pady=(10,0))

        l_name_label = Label(editor, text='Last Name')
        l_name_label.grid(row=1, column=0)

        address_label = Label(editor, text='Address')
        address_label.grid(row=2, column=0)

        city_label = Label(editor, text='City')
        city_label.grid(row=3, column=0)

        state_label = Label(editor, text='State')
        state_label.grid(row=4, column=0)

        pincode_label = Label(editor, text='Pincode')
        pincode_label.grid(row=5, column=0)



        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            pincode_editor.insert(0, record[5])

        # Create a save button to save edited record
        save_btn = Button(editor, text='Save Changes', command=update)
        save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=20, ipadx=131)


# Let's make the GUI

# Create text entry labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10,0))

l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)

address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)

city_label = Label(root, text='City')
city_label.grid(row=3, column=0)

state_label = Label(root, text='State')
state_label.grid(row=4, column=0)

pincode_label = Label(root, text='Pincode')
pincode_label.grid(row=5, column=0)

delete_box_label = Label(root, text='Select ID:')
delete_box_label.grid(row=9, column=0, pady=(50, 10))


#  Create Text entry fields
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1 )
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
pincode = Entry(root, width=30)
pincode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=(50, 10))


# Submit Button
submit_btn = Button(root, text='Add Record To Database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=103)

# Query button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=130)

# Create a Delete button
delete_btn = Button(root, text='Delete Record', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=130)

# Create an update button
update_btn = Button(root, text='Edit Record', command=edit)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


# Commit changes
connection.commit()

# Close connection
connection.close()

root.mainloop()