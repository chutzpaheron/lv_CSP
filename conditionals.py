# LV, period 7, if and else statements
#CONDITIONALS- let a code make decision on a true/false value
#BOOLEAN is just true or false only hold two values 

time = 14
day = "tuesday"

if time > 5 and time < 12: 
    print("GOOD MORNING")
    if day != "saturday" or day != "sunday":
        print("are you ready.")
elif time < 17:
    if day != "saturday" and day != "sunday":
        print("how was school?") #nested conditional example #will only display if between 5-8pm
    print("GOOD AFTERNOON")
elif time < 20:
    print("GOOD EVENING")
else: 
    print("GOOD NIGHT")

print("END CODE")

#ALL CONDITIONALS start with keyword if and then a boolean statement
#every time a piece of code ends with a colon the next line HAS to be indented
#they also typically end with an else statement
#it goes at the bottom in case the if statement is false
# < less than # > greater than # == EQUAL # <= LESS OR EQUAL # >= MORE OR EQUAL # ! NOT EQUAL
#last are LOGICAL OPERATORS (and, or, not) # AND works if both conditions are true # OR two or one must be true # NOT neither are true
#ELIF only happens if conditions above are false and conditions below are true
#hierarchy- IF > ELIF > ELSE (you can have more than one elif)



#NESTING- more things inside a thing #a conditional can be put inside another conditional