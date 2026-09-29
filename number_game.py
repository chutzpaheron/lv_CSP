# LV, period 7, random number game

import random

number = random.randint(1,100)
guesses = 1
guess = int(input("guess a number between 1 and 100:"))

while guesses <= 6:
    if guesses >= 6:
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
         print(f"correct! you guessed {number} in {guesses} tries!")
         break
    
    
    

        
    