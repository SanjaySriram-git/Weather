from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

root = Tk()
root.title("WEATHER APP")
root.geometry("900x500+300+200")
root.resizable(False, False)


# SEARCH BOX
search_image = PhotoImage(file="Copy of search.png")  
myimage = Label(root, image=search_image)  
myimage.place(x=20, y=20)

textfield = tk.Entry(
    root,
    justify="center",
    width=17,
    font=("arial", 25, "bold"),
    bg="#404040",
    border=0,
    fg="white"
)
textfield.place(x=50, y=40) 

search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(root,
                     image=search_icon,
                     borderwidth=0,
                     cursor="hand2",
                     bg="#404040",
                     
)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="Copy of logo.png")  
Logo = Label(root, image=Logo_image)  
Logo.place(x=150, y=100)  

# Bottom box
Bottom_box = PhotoImage(file="Copy of box.png")
BOTTOM = Label(root, image=Bottom_box)
BOTTOM.pack(padx=5, pady=5, side="bottom")

# Weather info labels
clock = Label(root, font=("arial", 20), fg="white", bg="#404040")
clock.place(x=30, y=100)

name = Label(root, font=("arial", 15), fg="white", bg="#404040")
name.place(x=30, y=130)

label1 = Label(root, text="WIND", font=('Helvetica', 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=('Helvetica', 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=('Helvetica', 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=('Helvetica', 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

root.mainloop()