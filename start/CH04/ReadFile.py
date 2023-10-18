#!/usr/bin/env python3
# Sample script that reads from a file
# By 
import os 
os_path = os.path.realpath(__file__)
dir_path = os.path.dirname(os_path)
#open fule for reading 
wopper = open(dir_path + "/Testing.txt", "r")
# read from the file
file_contents = wopper.read()
print(file_contents)
#close file 
wopper.close()
# = os.getcwd()


print(dir_path)