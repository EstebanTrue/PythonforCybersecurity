#!/usr/bin/env python3
# https://haveipeenpwned
#by Est

#imports
import hashlib
import requests
# have i been pwned():
    #shaw 1 split
    #call api
    #search results
def amiPwned(pPassword):
    prefix = pPassword[:5]
    body = pPassword[5:]
    #call api
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    #im not too sure how but filter theresults from the bottom
    #data = response.json()
    #specificPass = data[body]

    return specificPass.text


# sha 1 hash functions
def shaOneHash(hashPassword):
    hashObject = hashlib.sha1(hashPassword.encode())
    return hashObject.hexdigest()

#input
userPassword = input("what is the password your checking? ")
#call function from api
result = amiPwned(shaOneHash(userPassword))
#print results
print(f"Password found {result} times.")

