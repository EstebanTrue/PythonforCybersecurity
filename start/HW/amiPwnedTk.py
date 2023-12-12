import tkinter
import requests
import hashlib

def amiPwned(pPassword):
    prefix = pPassword[:5]
    body = pPassword[5:]
    body = body.upper()

    # Call the API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    pwndLines = response.text.splitlines()
    
    for line in pwndLines:
        if body in line:
            lineParts = line.split(":")
            return int(lineParts[1])

    # The code went through all the lines, and if it reaches here, the password is not found.
    return 0

def shaOneHash(hashPassword):
    hashObject = hashlib.sha1(hashPassword.encode())
    return hashObject.hexdigest()

def checkPassword():
    userPassword = password_entry.get()
    hashedPassword = shaOneHash(userPassword)
    result = amiPwned(hashedPassword)
    resultStr = '{:,}'.format(result)
    result_label.config(text=f"The Password - {userPassword} -, found {resultStr} times.")

    if result == 0:
        strength_label.config(text="AMAZING PASSWORD")
    elif result < 10:
        strength_label.config(text="You could do better")
    else:
        strength_label.config(text="Horrid password")


windowMain = tkinter.Tk()
windowMain.title("Password Checker")


password_label = tkinter.Label(windowMain, text="Enter Password:")
#pady moves it down
password_label.pack(pady=5)

password_entry = tkinter.Entry(windowMain)
password_entry.pack(pady=5)

check_button = tkinter.Button(windowMain, text="Check Password", command=checkPassword)
check_button.pack(pady=10)

result_label = tkinter.Label(windowMain, text="")
result_label.pack()

strength_label = tkinter.Label(windowMain, text="")
strength_label.pack()


windowMain.mainloop()