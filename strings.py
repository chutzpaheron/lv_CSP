# LV, period 7, strings

#datatypes are how we save different bits of info (integers hold whole numbers, floats hold decimals)
#strings are another datatype saved in quotes ("'both work'")

name = input("what is your name?:").strip().capitalize() #strip removes spaces

name2 = 'Other Name' #also a string
print(name + " " + "Last Name")

age = input("how old are you?:")
print(age + age)
print(type(age))

#age prints as a string despite being an integer and you cannot do math with it
#print(age * age) and (age / age) shows an error message
#print(age * 2) and (age + age) just gives you the string twice
#name.capitalize()
#"hello".lower()
#"this is csp".replace("csp", "math")
#string.action (method) ()

sentence = "the quick brown fox jumped over the lazy dog"
print(sentence)
print(sentence.replace("dog", "cat"))
print(len(name)) #len is short for length, tells you the amount of letters

print(f"your name is {name} which is {len(name)} letters long, your initial is {name[0]}, and i will call you {name[0:3]}") 

#F STRING!!!!! short for FORMATTED STRING
#the f string allows you to write code directly into a string
#{curly brackets} it allows the computer to tell what is important
# faster at referencing variables and writing equations within sentences

# name[] finds a specific character (index number)
#computers start counting at 0 so the second character would be 1
#SLICING- taking a big string and taking out a smaller piece
#the smaller piece is called a substring
# 0:2 only includes two characters because it cuts off at the third

