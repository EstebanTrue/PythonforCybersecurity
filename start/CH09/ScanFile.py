#!/usr/bin/env python3
# Script that scans files using VirusTotal
# https://developers.virustotal.com/reference
# By 

import configparser
import hashlib

def getApiKey(keyName):
    #create configparser object and load file
    config = configparser.ConfigParser()
    config.read("/home/justincase/secrets.ini")
    #get api key
    apiKey = config["APIKeys"][keyName]
    #returb value
    return apiKey

def hashFile(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

# get VT report
def getVtReport():
    import requests
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': '<apikey>', 'resource': '<resource>'}
    response = requests.get(url, params=params)
    print(response.json())

#get VT file upload
def scanVtFile():
    import requests
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': '<apikey>'}
    files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}
    response = requests.post(url, files=files, params=params)
    print(response.json())

# get api key
token = getApiKey("virustotal")
#main (need to add the secrets file to your computer)
fileToCheck = input("what file do you ewant to check")
fileHash = hashFile(fileToCheck)
print(fileHash)
