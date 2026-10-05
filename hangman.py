# LV, period 7, what is the capital of France? (autocomplete result)
# hangman

import random

with open("words.txt", "r") as file:
    list = file.read().split(",")

guesses = 6
word = random.choice(list)
right = 0
wrong = 0
letter = ""
guess = ""
max = 6

def display(word, guesses):
    for letter in word:
        if letter in guess:
            print("correct!")

def display_hangman():
 while guesses >= 6:
     if guesses == 6:
         print("""
 ______
|     |   
|     0
|    /|\
|    / \
|______""")
         print(f"you ran out of guesses! the word was {word}!")
     elif guesses == 5:
         print("""
 ______
|     |   
|     
|    /|\
|    / \
|______""")
     elif guesses == 4:
         print("""
 ______
|     |   
|     
|    / \
|    / \
|______""")
     elif guesses == 3:
         print("""
 ______
|     |   
|     
|    / \
|    / 
|______""")
     elif guesses == 2:
         print("""
 ______
|     |   
|     
|    / \
|     
|______""")
     elif guesses == 1:
         print("""
 ______
|     |   
|     
|    / 
|     
|______""")
     else:
         print("""
 ______
|     |   
|     
|     
|     
|______""")
         
letter = input("hello, welcome to hangman! guess a letter:")

while max >= guesses:
    for letter in word:
        if letter in word:
            display += letter
        else:
            display += "_ "




# ______
#|     |   
#|   (*-*)
#|    /|\
#|    / \
#|______

#write down ten words on a separate file
#create another which holds how many wins/how many losses user has (starts at 0)
#READ FILES
#use split(,) to create list and pull wins/losses
#BUILD GAME
#first show user site of the execution, then blanks
#SAVE WORD AS VARIABLE RANDOM.CHOICE(name of list)
# +variable for wrong guesses and what letters guessed

#build functions
#first just prints out display for user (letters spaces display)
#variable for display word, starts empty
#loop correct word (looks at every letter individually)
#if it is correct, add letter to display variable
#if its not guessed put underscore
#empty = 0 wrong, full = game over

#main loop (while true)
#show user scaffold (call function)
#ask user to guess
#check if not letter in word and increase incorrect guesses
#this increases the body parts somehow
#check if display word == actual word
#if they want to play again, reset everything
#if they have too many wrong, say they lost and the word