
import requests, os, time, json

#starting from the begining
def pinga(pingerUrl):
    #To ping the api its works to make a get request rather the ping command
    response = requests.get(pingerUrl)
    return response
    
def coinDataCol(colUrl):

    payload={}
    headers = {}

    response = requests.request("GET", colUrl, headers=headers, data=payload)

    return response.text

def timeChecker(timUrl):
    while True:
        #The try/except statement is easier then using the conditionals as well as lets me see if ther is a error
        try:
            if pinga(timUrl) == "<Response [200]>":
                print(coinDataCol(url))
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(30)

url = "https://api.coincap.io/v2/assets/bitcoin"

timeChecker(url)
