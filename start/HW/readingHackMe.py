#Write a python script that reads hackme.txt

#Print out "Here is someone to hack - information"

#Then print the various information found in the file

with open("hackme.txt", "r") as file:
    
    file_stuff = file.read()
    print(file_stuff)
