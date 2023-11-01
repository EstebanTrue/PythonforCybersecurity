#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By 

#1mports
import os
import crypt

#ask user for hashtype/salt and hashed password
hash_salt = input("what is the hashtype/salt?")
target_hash = input("what is the full hash?")
#ask which dictionary file to use
text_fil = input("what file do you want to print?")
text_file = "/" + text_fil
#open the dictionary file
os_path = os.path.realpath(__file__)
dir_path = os.path.dirname(os_path)
dictionary_file = open(dir_path + text_file, "r") 
dict_words = dictionary_file.readlines()
#loop through each password
for pass_guess in dict_words:
    #strip the /n because it was crypting that part too
    pass_guess = pass_guess.strip()
    print(pass_guess)
    # hash password
    guess_hash = crypt.crypt(pass_guess, hash_salt)
    #Compare hash with original hash
    if guess_hash == target_hash:
        print("Password found:{0}".format(pass_guess))
        exit()
print("Password not found: Try a different dictionary txt file")
    #if match, print and quit
#no match found, print failure message
