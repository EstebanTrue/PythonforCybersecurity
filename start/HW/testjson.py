#!/usr/bin/env python3
import requests
import json

requestUri = "https://www.reddit.com/.json"
requestHeaders = { 'User-agent': 'IT102 bot' }
payload = {}    
r = requests.get( 
   requestUri, 
   headers = requestHeaders,
   data = payload
   )

if r.status_code == 200:
   data = r.json()
   print(data['data']['children'][0]['data']['ups'])
else:
   print("Error, status code: {} - {}".format(r.status_code, r.content))
