#!/usr/bin/env python3
# Third example of pinging from Python
# By 
#Testing Testing 123

#import modules
import os

def ping_uh(ipAd):
    
    
    ping_cmd = "ping -c 1 -w 1 " + ipAd + " > /dev/null 2>&1 "
    exit_code = os.system(ping_cmd)

    #returns results of the number that determindes whiether a ip address is online or not (only one return silly )
    
    return exit_code

   


#build the ping command 
pre_target = "192.168.0." 

#run ping command


for x in range(3):
    post_target = 1 + x
    target = pre_target + str(post_target)

    exit_code = ping_uh(target)
    #print results
    

    if exit_code == 0:
        print("*****{0} User is Active****" .format(target))

    if exit_code != 0:
        print("{0} User is not online" .format(target)) 

test = ping_uh("192.168.0.4")
print(test)