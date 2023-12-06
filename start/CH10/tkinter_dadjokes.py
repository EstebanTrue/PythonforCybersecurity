# third tkinter script
# Dad Joke
# Create by 

# Import tkinter
import tkinter
import requests
# Functions
def getDadJoke():
    
    api_url = "https://icanhazdadjoke.com/"

    headers = {
        'Accept': 'application/json',
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        joke_data = response.json()

        joke = joke_data['joke']
        print("Random Dad Joke:")
        print(joke)
    else:
        print("Error, status code:", response.status_code)

    labelJoke.config(text = joke)
# Create the GUI main window
windowMain = tkinter.Tk()
# Add widgets
labelJoke = tkinter.Label(windowMain,  \
    text="Get dad joke", \
    font=("Arial Bold", 50))
buttonJoke = tkinter.Button(windowMain, \
    text="Get dad joke", \
    command= getDadJoke)
labelJoke.pack()
buttonJoke.pack()
# Enter the main event loop
windowMain.mainloop()
