from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from datetime import*
import time
from math import*

# Create class Clock
class Clock:
    # Define constructor for Clock.
    def __init__(self, root):
        self.root = root
        self.root.title('GUi Analog Clock')
        self.root.geometry('1520x800+2+2')
        self.root.config(bg='#021e2f')

        # Heading for Project.
        title = Label(self.root, text='Analog Clock- By Sthita Pragyan Khilar', 
                      font=("times new roman", 50, "bold"), 
                      bg='#04444a', fg='white')
        
        title.place(x=0, y=50, relwidth=1)
        
        # Label for clock picture 
        self.lbl = Label(self.root, bg='white', bd=20, relief='raised')
        self.lbl.place(x=550, y=250, height=400, width=400)

        self.working()


    def clock_image(self, hr, min_, sec_):
        
        #===== For Clock Image ====#
         
        # Create a new image object with 'RGB' mode, size 400x400 pixels, 
        # and white background color.
        clock = Image.new('RGB', (400,400), (255, 255, 255))

        # Create an ImageDraw object associated with the 'clock' image to allow drawing operations.
        draw = ImageDraw.Draw(clock)

        # Imposing clock.png on clock_new.png
        # Open clock.png
        bg = Image.open('D:/forgithub/Projects/icons and images/clock.png')

        # resize clock.png to fit 'draw', LANCZOS or ANTIALIAS in the previous versions
        # are used to preserve the image qualithy when we resize them.
        bg = bg.resize((300, 300), Image.LANCZOS)

        # Finally impose clock.png on draw.
        clock.paste(bg,(50, 50))

        #======= For Lines =======#
        origin = 200,200
        # Hour hand
        draw.line((origin, 200+80*sin(radians(hr)), 200-80*cos(radians(hr))), fill='black', width=4)

        # Minute hand
        draw.line((origin, 200+120*sin(radians(min_)), 200-120*cos(radians(min_))), fill='black', width=3)

        # Seconds hand
        draw.line((origin, 200+120*sin(radians(sec_)), 200-120*cos(radians(sec_))), fill='red', width=1)


        # Save the generated image to the specified file path.
        clock.save('D:/forgithub/Projects/icons and images/clock_new.png')


    def working(self):   
        # Fetch the current hour, minute and seconds from system.
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        # Convert the time into degrees.
        hr = (h/12)*360
        min_= (m/60)*360
        sec_ = (s/60)*360

        # Call self.clock_image to update the clock hands based on the current time.
        self.clock_image(hr, min_, sec_)
        
        # Open the clock_new image.
        self.img = ImageTk.PhotoImage(file='D:/forgithub/Projects/icons and images/clock_new.png')

        # And update the Label widget with the new clock image.
        self.lbl.config(image=self.img)

        # Recursive call to itself after 200 miliseconds to keep updating time.
        self.lbl.after(200, self.working)

root = tk.Tk()
obj = Clock(root)
root.mainloop()







# Notes
'''
Image.new('RGB', (400, 400), (255, 255, 255)):
-----------------------------------------------
Image Mode ('RGB'): Creates a blank image in RGB mode (Red, Green, Blue), 
which supports color images.

Size ((400, 400)): Specifies the width and height of the image in pixels. 
In this case, the image will be 400x400 pixels.

Background Color ((255, 255, 255)): This is the color of the image's background.
The tuple (255, 255, 255) represents the color white in the RGB color system.
'''

'''
ImageDraw.Draw(clock):
----------------------
This creates a draw object that allows you to perform various drawing operations on the clock image.

The draw object provides a range of methods such as line(), rectangle(), ellipse(), text(), etc., 
which you can use to draw shapes, lines, or text on the image.

The drawing operations are performed directly on the image (clock), 
modifying it in memory.
'''

'''

Formula to Rotate the Clock(Anti-clockwise)
-------------------------------------------

angle_in_radians = angle_in_degrees * math.pi/180,
converting the angle from degrees to radians because trigonometric 
functionns(sin and cos) in python's math module expect the angle to be in radians,
 not degrees.

line_length = some value

center_x = some value

center_y = some value 

end_x = center_x + line_length * math.sin(angle_in_radians)

end_y = center_y - line_length * math.cos(angle_in_radians)

'''