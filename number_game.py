# LV, period 7, random number game

import random

number = random.randint(1,101)
guesses = 0
guess = int(input("guess a number:"))

while guesses <= 7:
    if guesses >= 7:
         print(f"you ran out of tries! the number was {number}!")
         break
    elif number < guess:
        print(f"{guess} is bigger than the number!")
        guesses = guesses + 1
        guess = int(input("guess another number:"))
    elif number > guess:
        guesses = guesses + 1
        print(f"{guess} is smaller than the number!")
        guess = int(input("guess another number:"))
    else:
         print(f"correct! {number} is the number!")
         break
    
    
    

        
    