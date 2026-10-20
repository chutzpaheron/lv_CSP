#LV, period 7, theater
#what is a matinee
#manatee. The Manatee

def hi():
    while True:
        try:
            amount = int(input("enter your age: "))
            return amount 
        except:
            print("please insert a whole number!")

age = hi()

if age < 5:
    price = 0
elif age < 13:
    price = 8
elif age < 65:
    price = 12
else:
    price = 9

matinee = input("are you attending a matinee? (YES or NO): ").lower().strip()

while True: #HELP OVER HERE
    if matinee == "yes":
        if price == 0:
          price == price - 0
    elif matinee == "no":
     price = price - 3
    else:
     print("invalid input!")

print(f"the ticket will cost ${price}")
