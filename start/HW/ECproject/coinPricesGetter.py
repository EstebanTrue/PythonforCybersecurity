#!/usr/bin/env python3
# By Esteban Trujillo

# The imports look nice this way
import requests, os, time, json, hashlib

os_path = os.path.realpath(__file__)
dir_path = os.path.dirname(os_path)
salt = "G.DTW7g9s5U7KYf5"
#starting from the begining
#pinging api
def whatCoin(urlW):
    coinW = input("What coin do you want information on? ")
    selectiveUrl = urlW,"/",coinW
    return selectiveUrl

def pinga(pingerUrl):
    #The try statement is easier then using the conditionals 
    #To ping the api its works to make a get request rather the ping command
    try:
        response = requests.get(pingerUrl)
        return f"***API at {pingerUrl} is online.***"
    except: 
        return f"API at {pingerUrl} is not online."

#sha 1 hashing for passwords
def shaOneHash(password,saltHash):
    securePass = password + saltHash
    hashObject = hashlib.sha1(securePass.encode())
    return hashObject.hexdigest()

# this is gonna be the password and username loaded to a file
def userCreds(saltCred):
    userD = dict()
    username = input("What is your username: ")
    userPass = input("What is your password: ")
    newPass = shaOneHash(userPass, saltCred)
    userD[username] = newPass
    return userD

#Gettting data from api
def coinDataCol(colUrl):
    #what we store the data in
    payload={}
    headers = {}
    #Gets the data for us from our api
    response = requests.request("GET", colUrl, headers=headers, data=payload)
    #returns the data
    return response.text

#filter through the data
def oCoinData(ocdUrl):
    #organize data with 
    coinData = coinDataCol(ocdUrl)

#returns data however many seconds someone wants                                                      
def timeChecker(timUrl):
    timer = int(input("How many seconds do you want to wait for your data to be returned: "))
    while True:
        # The try/except statement is easier than using the conditionals, as well as lets me see if there is an error
        try:
            #comparing the ping to a active status
            if pinga(timUrl) == f"***API at {timUrl} is online.***":
                # will print data howeverlong the sleep is 
                print(coinDataCol(timUrl))
        # This will show us any errors if they occur
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(timer)
# the timeOut function is now optional wiht the =0
def authentic(filePath, saltA, userA, authUrl, timeOut=0):
    with open(filePath, "r") as passwordFile:
        for line in passwordFile:
            try:
                #loads the data into a dictionary
                user_data = json.loads(line)
                #finds key
                key = list(user_data.keys())[0]
                # gets password from the key
                val = user_data[key]
                # Allows up to 5 tries until the user is kicked from the program
                for retry in range(5):
                    if userA == key:
                        # asks for password again
                        authenticate = input("Enter your Password: ")
                        #salts new password
                        testPass = shaOneHash(authenticate, saltA)
                        #compares password to the one saved in the file
                        if testPass == val:
                            #if password is correct runs the program
                            timeChecker(authUrl)
                        else:
                            print("Wrong Password. Try again silly... Think and retry when it asks!")
                            time.sleep(timeOut)
                            timeOut += 5

                else:
                    print("slow your horsies cowboy thats way too many attempts.Bye, Bye")
                    #exits the user from the program
                    exit(1)


            except json.JSONDecodeError:
                # Handle the case where the line doesn't have the expected JSON format
                print(f"Skipping line '{line.strip()}'. It doesn't have the expected JSON format.")
                # You can log the issue or take other actions as needed

    print("Authentication failed. User or password not found.")


url = "https://api.coincap.io/v2/assets"
#timer = int(input("How long do you want to wait for your data to be returned: "))

#put the function into a readable variable
user_credentials = userCreds(salt)
#To put the file in the same folder as mine
userCred_Fpath = os.path.join(dir_path, 'users.txt')
#puts the credentials into a file named users.txt
with open(userCred_Fpath, 'w') as convert_file: 
     convert_file.write(json.dumps(user_credentials))
# getting the username from the Dictionary 
if user_credentials:
    username = list(user_credentials.keys())[0]
    theUser = username
please_work = whatCoin(url)
authentic(userCred_Fpath, salt, theUser, please_work)



# results - 
# {"data":{"id":"bitcoin","rank":"1",***"symbol":"BTC",***"name":"Bitcoin","supply":"19563700.0000000000000000","maxSupply":"21000000.0000000000000000",
# "marketCapUsd":"849889053338.5837237911056500","volumeUsd24Hr":"7288795573.5881609602264709",***"priceUsd":"43442.1430168415853745",
# "changePercent24Hr":"-1.1319457196120539","vwap24Hr":"43444.3009109860750579","explorer":"https://blockchain.info/"},"timestamp":1702000460232}