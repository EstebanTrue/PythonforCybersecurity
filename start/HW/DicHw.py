#!/usr/bin/env python3
#by Estebn 

import os
import crypt

# Open shadow file
os_path = os.path.realpath(__file__)
dir_path = os.path.dirname(os_path)
shadowFile = open(dir_path + "/shadow", "r")

# Read lines and extract hashes
lines = shadowFile.readlines()
hashes = []
users = []
for line in lines:
  if "hackme" in line:
    hash_salt = line.split(":")[1]
    username = line.split(":")[0]
    hashes.append(hash_salt)
    users.append(username)

# Load password dictionary 
passwords = open(dir_path+"/top1000.txt", "r").readlines()

# Crack passwords
 

for i, hash_salt in enumerate(hashes):  
    username = users[i]  
    real_hash = hash_salt.split("$")[2]
    ultrareal_hash = "$6$"+ real_hash + "$"
    for password in passwords:
        test_hash = crypt.crypt(password.strip(), ultrareal_hash)
        if test_hash == hash_salt:
            print("[+] Cracked password for {}: {}".format(username, password))
            break
    else:
        print("[-] Failed to crack password for {}".format(username))
