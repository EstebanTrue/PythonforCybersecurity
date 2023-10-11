#!/usr/bin/env python3
# First example of pinging from Python
# By 

#import modules
import os
#build the ping command 
target = "192.168.0." 

#run ping command
for x in range(255):
    count = 1 + x
    fullA = target + str(count)
    ping_cmd = "ping -c 1 -w 1 " + fullA + " > /dev/null 2>&1 "
    exit_code = os.system(ping_cmd)
    #print results
    #print(fullA, exit_code)

    if exit_code == 0:
        print("*****{0} User is Active****" .format(fullA))

    if exit_code != 0:
        print("{0} User is not online" .format(fullA))
