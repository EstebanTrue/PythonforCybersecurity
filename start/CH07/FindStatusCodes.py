#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By 

import os
import re

os_path = os.path.realpath(__file__)
dir_path = os.path.dirname(os_path)
logFile = open(dir_path + "/access.log", "r")

ipDict = {}
#setup regeex pattern
statusPattern = r'\s(\d{3})\s'
statusDict = {}
while True:
    line = logFile.readline()
    if not line:
        break
    m = re.search(statusPattern, line)
    if m:
        code = m.group()
        if code in statusDict.keys():
            statusDict[code] += 1
        else:
            statusDict[code] = 1
   
logFile.close()
for w in sorted(statusDict, key = statusDict.get, reverse = False):
    print(w, statusDict[w])