# LV, period 7, random number game

import random

guess = int(input("guess a number:"))


number = random.randint(1,101)
guesses = 0

print(number) #REMOVE

while guesses >= 6:
    if number == guess:
        print(f"correct! {number} is the number!")
    elif number > guess:
        guesses = guesses + 1
        print(f"")