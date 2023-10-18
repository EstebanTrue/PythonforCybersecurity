#!/usr/bin/env python3
# Sample script that writes to a file
# By 

#open and create a file
wopper = open("Testing.txt", "w")
#write the file 
wopper.write("file\n")
wopper.write("I am Desperado")
name = input("State thy name?\n")
wopper.write("WHO ARE YOU TO ANSWER AND OPEN THIS FILE\n")
piece = input("ANSWER OR FACW THE CONSEQUENSES\n")
if piece == "im sorry":
    
#close the file 
wopper.close()