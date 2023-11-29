
import random

print("what are your top 3 Curse words!")
first = input("1: ")
second = input("2: ")
third = input("3: ")
print("\n")

words = []
words.append(first)
words.append(second)
words.append(third)


phrases = [f"i will give you a {words[0]} whooping\n",  f"dont be such a {words[1]}-tard\n", f"your a {words[2]} face\n"]


for eachPhrase in range(10):
    random.shuffle(words)
    random.shuffle(phrases)
    randomPhrase = random.choice(phrases)
    print(randomPhrase)