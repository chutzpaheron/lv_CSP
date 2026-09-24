# LV, period 7, password checker
#im not sure if this is how you wanted it done but if it works it works

charactercount = False
upper = False
lower = False
numbers = False
symbols = False
strength = 0

password = input("what is your password?:")

if len(password) >= 8:
        charactercount = True

for letter in password:

    if letter.isupper():
        upper = True

    if letter.islower():
        lower = True

    if letter.isnumeric():
        numbers = True

    if letter in "~!@#$%^&*()_+|:<>?-=[],./":
        symbols = True

if charactercount == True:
    strength = strength + 1
    print("your password has over eight characters. [1 point!]")
else:
      print("your password is under eight characters!")

if upper == True:
    strength = strength + 1
    print("your password has at least one uppercase letter. [1 point!]")
else:
      print("your password is missing uppercase letters!")

if lower == True:
    strength = strength + 1
    print("your password has at least one lowercase letter. [1 point!]")
else:
      print("your password is missing lowercase letters!")
    
if numbers == True:
    strength = strength + 1
    print("your password has at least one number. [1 point!]")
else:
      print("your password is missing numbers!")

if symbols == True:
    strength = strength + 1
    print("your password has at least one special character. [1 point!]")
else:
      print("your password is missing symbols!")

if strength == 5:
    print("you have a STRONG password!")
elif strength > 2 and strength < 5:
    print("you have a MEDIUM password!")
else:
    print("you have a WEAK password!")
