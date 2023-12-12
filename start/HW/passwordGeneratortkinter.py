import tkinter, random

def passwordGenerator():
    print("Password Generator:")
    useUppercase = input("Do you want to include uppercase characters? (y/n): ").lower() == 'y'
    useLowercase = input("Do you want to include lowercase characters? (y/n): ").lower() == 'y'
    useSymbols = input("Do you want to include symbols? (y/n): ").lower() == 'y'
    useNumbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'

    characters = []
    if useUppercase:
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if useLowercase:
        characters.extend('abcdefghijklmnopqrstuvwxyz')
    if useSymbols:
        characters.extend('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    if useNumbers:
        characters.extend('0123456789')

    psword = ''.join(random.choice(characters) for _ in range(10))
    
    labelPassG.config(text=psword)

windowMain = tkinter.Tk()

labelPassG = tkinter.Label(windowMain,  \
    text="Get your own password", \
    font=("Arial Bold", 50))
labelPassG.pack()

windowMain.mainloop()