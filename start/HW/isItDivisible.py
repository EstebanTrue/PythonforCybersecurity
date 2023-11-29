#!/usr/bin/env python3
# is it divisible by x?
#by Esteban Trujillo

def isDivisible(pnumber, pdivisor):
    if pnumber % pdivisor == 0:
        return f"{number} is divisible by {divisor}"
        #return True
    else:
        return f"{number} is NOT divisible by {divisor}"
        #return False
    
number = int(input("what is the number: "))
divisor = int(input("what is the divisor: "))
result = isDivisible(number, divisor)
print(result)
