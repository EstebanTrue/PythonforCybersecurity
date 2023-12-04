# First tkinter script
# Create by 

# Import tkinter
import tkinter
# Create the GUI main window
windowMain = tkinter.Tk()
# Add widgets
labelHello = tkinter.Label(windowMain, \
    text="hwllo Wwrld", \
    font= ("D050000L", 180) \
    bg= 'red' )
labelHello.pack()

# Enter the main event loop
windowMain.mainloop()
