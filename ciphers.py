# LV, period 7, caesar cipher

crypt = input("would you like to encrypt or decrypt a message? type in E or D:")
message = input("type in a message:")
shift = int(input("by how much is it shifted?:"))

for character in message:
  if character.islower():
     print(ord(character))
  elif character.isupper():
     print(ord(character))
  else:
    print(ord(character))

#encrypt and decrypt messages in the function
#write code first, function later
#1 write all variables
#2 make a loop which prints out all letters
#3 make a conditional inside loop to check if characters are in alphabet
#if its in alphabet, convert into ascii number, increase/decrease, convert back, output is ciphered
#4 to not print out letters individually, put all in one string
#have a variable where you save each of the letters
#they dont change if theyre not letters
#5 if it wraps over, check before reconverting to take to the start of the alphabet
#THIS IS ALL TO ENCRYPT!!
#to decrypt it is basically the same, literally just turn the number into a negative

#number += 2 #by how much the cipher shifts
#print(f"the letter {lower_start} matches to the number {ord(lower_start)}") #ORD converts letter into its ascii digit
#print(f"the letter {chr(number)} matches to the number {number}") #CHR converts into ascii number
#print(f"the letter {lower_end} matches to the number {ord(lower_end)}")