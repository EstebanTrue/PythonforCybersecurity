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
    body = body.upper()
    #call api
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    #im not too sure how but filter theresults from the bottom
    #data = response.json()
    #specificPass = data[body]

    #print(response.text)
    pwndLines = response.text.splitlines()
    
    for line in pwndLines:
        if body in line:
            lineParts = line.split(":")
            return lineParts[1] 
    #The code went through all the lines and thats why if it hits the last line it will return 0
    return 0

# sha 1 hash functions
def shaOneHash(hashPassword):
    hashObject = hashlib.sha1(hashPassword.encode())
    return hashObject.hexdigest()

if __name__ == "__main__":
    #input
    userPassword = input("what is the password your checking? ")  
        #call function from api
        #its a number because the comma cunction doesnt work without it
        #result = int(amiPwned(shaOneHash(userPassword)))
    result = int(amiPwned(shaOneHash(userPassword)))
        #adding commas
    res = '{:,}'.format(result)
        #print results
        #print(f"The Password - {userPassword}  -, found {res} times.")
    print(f"The Password - {userPassword}  -, found {res} times.")


    if result == 0:
        print("AMAZING PASSWORD")
    elif result < 10:
        print("you could do better")
    else:
        print("horrid password")
