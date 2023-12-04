# Seconder tkinter script
# Add a button and command
# Create 

# Import tkinter
import tkinter
from tkinter import messagebox
# Functions
def buttonHelloClick():
    tkinter.Label(windowMain, text="hi :)").grid(column=1, row=1)
    message = entryMessage.get()
    labelHello.config(text=":)")
    messagebox.showerror("Nuh-uh-uhhh", message)
# Create the GUI main window
windowMain = tkinter.Tk()
# Add widgets
labelHello = tkinter.Label(windowMain, \
    text= "Hello there", \
    font=("Arial Bold", 90))
    #you cant use both ppack and grid in the same window because it wont work
#labelHello.pack()
labelHello.grid(column=0, row=0)
#button
buttonHello = tkinter.Button(windowMain, \
    text= "click here", \
    command= buttonHelloClick) #.pack()
buttonHello.grid(column=1, row=0)
#text box
entryMessage = tkinter.Entry(windowMain, width=50)
#the grid must be seperate or the computer will be wierd about itand not work 
entryMessage.grid(column=0, row=2)

# Enter the main event loop
windowMain.mainloop()