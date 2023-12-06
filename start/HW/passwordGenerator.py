import random
from amIPwned import shaOneHash
from amIPwned import amiPwned
def passwordGenerator():
    print("Password Generator:")
    useUppercase = input("Do you want to include uppercase characters? (y/n): ").lower() == 'y'
    useLowercase = input("Do you want to include lowercase characters? (y/n): ").lower() == 'y'
    useSymbols = input("Do you want to include symbols? (y/n): ").lower() == 'y'
    useNumbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'

    characters = []
    if useUppercase:
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if useLowercase:
        characters.extend('abcdefghijklmnopqrstuvwxyz')
    if useSymbols:
        characters.extend('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    if useNumbers:
        characters.extend('0123456789')

    psword = ''.join(random.choice(characters) for _ in range(10))

    return psword

password = passwordGenerator() 
print(f"Generated password - {password}")

result = int(amiPwned(shaOneHash(password)))
res = '{:,}'.format(result)

print(f"The Password - {password}  -, found {res} times.")


if result == 0:
    print("AMAZING PASSWORD")
elif result < 10:
    print("you could do better")
else:
    print("horrid password")

