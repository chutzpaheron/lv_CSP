# LV, period 7, LOOPS
#a loop is something that repeats

import random

count = 1
while count <= 42:
    print(count)
    count += 1

#one loop is completed when it reaches a new integer
#last line is increasing the iterator

duck = 1 #start
goose = random.randint(1,43) #must import random to do this

while True: #because there is no defined end point
    if duck == goose: #endpoint
        break #ends loop
    print("duck...")
    duck += 1 #this is the same as [ducks = ducks + 1] #increase
print("GOOSE!!!")

#WHAT MAKES A LOOP#
#1- start point (usualy a variable outside loop)
#2- set a stopping point, will ALWAYS be a boolean #once it is false it stops
#3- increase iterator (RAIN WORLD REFERENCE) #each time around the loop is one iteration
#    _----_
#  /        \
# | *  ^  *  |
#  \        /  
#    --__--

#new word- CONTINUE
#it sends the code to the start of the loop (restarting)

birds = ["finch", "bunting", "magpie", "roadrunner", "hummingbird"] #my siblings btw
print(birds) #Print My Birds #looks exactly like the code
print(birds[2]) #prints magpie #REMEMBER INDEXES START AT 0

#COMPLEX DATA TYPES hold more stuff inside them (russian nesting doll)
#list, every item must be separate with commas
#and all items must be a valid datatype, words (strings) must have quotes


