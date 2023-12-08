#!/usr/bin/env python3

import requests, os, time, json

#starting from the begining
def pinga(pingerUrl):
    #The try statement is easier then using the conditionals 
    #To ping the api its works to make a get request rather the ping command
    try:
        response = requests.get(pingerUrl)
        return f"***API at {pingerUrl} is online.***"
    except: 
        return f"API at {pingerUrl} is not online."
    
def coinDataCol(colUrl):

    payload={}
    headers = {}

    response = requests.request("GET", colUrl, headers=headers, data=payload)

    return response.text

def oCoinData():
    #organizedata with json format p 384

def timeChecker(timUrl):
    while True:
        #The try/except statement is easier then using the conditionals as well as lets me see if ther is a error
        try:
            if pinga(timUrl) == f"***API at {timUrl} is online.***":
                print(coinDataCol(url))
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)

url = "https://api.coincap.io/v2/assets/bitcoin"

timeChecker(url)

# results - 
# {"data":{"id":"bitcoin","rank":"1","symbol":"BTC","name":"Bitcoin","supply":"19563700.0000000000000000","maxSupply":"21000000.0000000000000000",
# "marketCapUsd":"849889053338.5837237911056500","volumeUsd24Hr":"7288795573.5881609602264709","priceUsd":"43442.1430168415853745",
# "changePercent24Hr":"-1.1319457196120539","vwap24Hr":"43444.3009109860750579","explorer":"https://blockchain.info/"},"timestamp":1702000460232}