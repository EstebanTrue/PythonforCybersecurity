#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By 

import os
import re

os_path = os.path.realpath(__file__)
dir_path = os.path.dirname(os_path)
logFile = open(dir_path + "/access.log", "r")

ipDict = {}
statusDict = {}
while True:
    line = logFile.readline()
    if not line:
        break

    # check for 404
    if "404" in line:
        lineParts = line.split()
        ipAddr = lineParts[0]
        if ipAddr not in ipDict.keys():
            ipDict[ipAddr] = 1
        else:
            ipDict[ipAddr] += 1
logFile.close()
for w in sorted(ipDict, key = ipDict.get, reverse = False):
    print(w, ipDict[w])