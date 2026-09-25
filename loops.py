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
#1- start point (usually a variable outside loop)
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

#NOTES DAY TWO#

temperature = [30, 32, 29, 26, 38, 27, 32]
print(temperature)

#for temp in temperature: #this code broke idk why
#    total += temp

#average = total / len(temperature)
warmest = max(temperature)
coldest = min(temperature)

#print(f"the average temperature this week was {average:.1f} celsius")
print(f"the warmest temperature this week was {warmest} celsius")
print(f"the warmest temperature this week was {coldest} celsius")

#for loops- keyword to start is FOR
#next is the variable for the current iteration
#loop 1 is 3, loop 2 is 6, etc if youre counting multiples of 3
#next is IN #another keyword for this loop
#next is a list, you will always reference a list

for num in range(1,101):
    if num % 15 == 0: 
        print("FIZZBUZZ!!!!")
    elif num % 3 == 0:
        print("FIZZ!!")
    elif num % 5 == 0:
         print("BUZZ!!") #I KNEW WE WERE GOING TO DO THIS EVENTUALLY

#range makes a list automatically #you just set the range and count
#putting another number next to the other two gives you number in the list that many intervals away

birds = ["finch", "bunting", "magpie", "roadrunner", "hummingbird"] 
print(birds[2]) 

birds.append("oriole")
print(birds)

#append adds to the end of a list
#insert places it in a specific place
#pop removes an item
#if it is not indexed it removes the last item

newbird = input("say a bird:").strip().lower()
birds.append(newbird)
birds.insert(3, newbird) # remember this is indexed so it starts at zero
birds.pop(2)
print(birds)

#you can use for loops to print each item separately

for bird in birds:
    print(bird)

#100 LINES

