from tkinter import*
from PIL import ImageTk, Image


root = Tk()
root.title('Image Viewer')
#root.iconbitmap(r'D:\Tut\learn_Tkinter\icons\img_viewer.ico')
# In the above line I have used a raw string so that python doesn't confuse my backslashes with escape characters.


my_img1 = ImageTk.PhotoImage(Image.open(r'D:\Tut\learn_Tkinter\icons and images\Image1.jpeg'))
my_img2 = ImageTk.PhotoImage(Image.open(r'D:\Tut\learn_Tkinter\icons and images\Image2.jpeg'))
my_img3 = ImageTk.PhotoImage(Image.open(r'D:\Tut\learn_Tkinter\icons and images\Image3.jpeg'))
my_img4 = ImageTk.PhotoImage(Image.open(r'D:\Tut\learn_Tkinter\icons and images\Image4.jpeg'))
my_img5 = ImageTk.PhotoImage(Image.open(r'D:\Tut\learn_Tkinter\icons and images\Image5.jpeg'))
my_img6 = ImageTk.PhotoImage(Image.open(r'D:\Tut\learn_Tkinter\icons and images\Image6.jpeg'))
my_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

# This is a status bar:
status = Label(root, text = 'Image 1 of '+str(len(my_list)), bd=2, relief=SUNKEN, anchor=E)

label = Label(root, image=my_img1)
label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global label
    global forward_button
    global back_button

    label.grid_forget()
    label  = Label(image=my_list[image_number-1])
    forward_button = Button(root, text='>>', command=lambda:forward(image_number+1))
    forward_button.grid(row=1, column=2, pady= 5)
    back_button = Button(root, text='<<', command=lambda:back(image_number-1))

    if image_number == len(my_list):
        forward_button = Button(root, text='>>', state=DISABLED)


    back_button.grid(row=1, column=0, pady=5)
    forward_button.grid(row=1, column=2, pady=5)
    label.grid(row=0, column=0, columnspan=3)
    #update status bar
    status = Label(root, text='Image'+ str(image_number)+ 'of' + str(len(my_list)), bd=2, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E, pady=10)


def back(image_number):
    global label
    global forward_button
    global back_button

    label.grid_forget()
    label = Label(image=my_list[image_number - 1])
    forward_button = Button(root, text='>>', command=lambda: forward(image_number + 1))
    forward_button.grid(row=1, column=2, pady=5)
    back_button = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 1:
        back_button = Button(root, text='<<', state=DISABLED)

    back_button.grid(row=1, column=0, pady=5)
    forward_button.grid(row=1, column=2, pady=5)
    label.grid(row=0, column=0, columnspan=3)
    #update status bar
    status = Label(root, text='Image'+ str(image_number)+ 'of' + str(len(my_list)), bd=2, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E, pady=10)


back_button = Button(root, text='<<', command=back,state=DISABLED)
back_button.grid(row=1, column=0, pady= 5)

exit_button = Button(root, text='Exit', command=root.quit)
exit_button.grid(row=1, column=1, pady= 5)

forward_button = Button(root, text='>>', command=lambda:forward(2))
forward_button.grid(row=1, column=2, pady= 5)

# Packing the status bar
status.grid(row=2, column=0, columnspan=3,sticky=W+E)

root.mainloop()