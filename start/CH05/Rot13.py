#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By 
def teach_number_converter():
    message = input("Enter a message: ")
    message = message.lower()
    for letter in message:
        # turn letter to number (aski index)
        letter_number = ord(letter)
        # if less then 110 (n), add 13
        if letter_number >= 97 and letter_number <= 122:
            if letter_number < 110: 

                new_letter_number = letter_number + 13
            else:
                new_letter_number = letter_number - 13

        else:
            new_letter_number = letter_number
        # converting the number back to a character
        new_letter = chr(new_letter_number)
        
        print(new_letter, end="")




def my_number_converter():
    message = input("Enter a message: ")
    for letter in message:
        # turn letter to number (aski index)
        letter_number = ord(letter)
        # if less then 110 (n), add 13
        if letter_number < 110:
            new_letter_number = letter_number + 13
        else:
            new_letter_number = letter_number - 13

        if letter_number < 90:
            if letter_number < 78:
                new_letter_number = letter_number + 13
            else:
                new_letter_number = letter_number - 13
        # converting the number back to a character
        new_letter = chr(new_letter_number)
        
        print(new_letter, end="")

teach_number_converter()


#print(ord("a"))-- letter to a number
#print(chr("97"))-- number to letter