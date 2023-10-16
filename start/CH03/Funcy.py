#!/usr/bin/env python3
# example workign with Functions
#By 

#Create Functions

def multiply(first_num, sec_num):
    result = first_num * sec_num
    #print(result)
    return result

num1 = int( input("First Number: "))
num2 = int( input("Second Number: "))
#print(num1 * num2)
num3 = multiply(num1, num2)
print(num3)
