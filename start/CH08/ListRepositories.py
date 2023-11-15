#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By 

import requests
import configparser

def getApiKey(keyName):
    #create configparser object and load file
    config = configparser.ConfigParser()
    config.read("/home/justincase/secrets.ini")
    #get api key
    apiKey = config["APIKeys"][keyName]
    #returb value
    return apiKey

url = "https://api.github.com/user/repos"
token = getApiKey("Github")
payload={}
headers = {
  'Authorization': 'Bearer ' + token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
