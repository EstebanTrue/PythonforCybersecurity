with open("hackme.txt", "w") as file:
    name = input("What is your name? ")
    file.write(f"Name: {name}\n")
    
    favorite_color = input("What is your favorite color? ")
    file.write(f"Favorite Color: {favorite_color}\n")
    
    first_pet_name = input("What was your first pet's name? ")
    file.write(f"First Pet's Name: {first_pet_name}\n")
    
    maiden_name = input("What is your mother's maiden name? ")
    file.write(f"Mother's Maiden Name: {maiden_name}\n")
    
    elementary_school = input("What elementary school did you attend? ")
    file.write(f"Elementary School: {elementary_school}\n")

print("Information has been saved to hackme.txt.")