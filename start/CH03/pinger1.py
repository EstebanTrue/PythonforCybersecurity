#!/usr/bin/env python3
# First example of pinging from Python
# By 

#import modules
import os
#build the ping command 
target = "127.0.0." 

#run ping command
for x in range(255):
    count = 1 + x
    fullA = target + str(count)
    ping_cmd = "ping -c 1 -w 1 " + fullA
    os.system(ping_cmd)
    print(x)
#print results