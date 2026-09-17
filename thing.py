# LV, period 7, budget assignment

while True:
    try:
        income = float(input("what is your monthly income?:"))
        break
    except:
        print("enter a number!!!! rebukes you for not entering a number") #spaghetti code...
#is this spaghetti code actually idk
while True:
    try:   
        rent = float(input("what is your monthly rent?:"))
        break
    except:
        print("enter a number!!!! rebukes you for not entering a number")

while True:
        try:
            utilities = float(input("what is your monthly utilities?:"))
            break
        except:
                print("enter a number!!!! rebukes you for not entering a number")

while True:
        try:
            groceries = float(input("what is your monthly groceries?:"))
            break
        except:
            print("enter a number!!!! rebukes you for not entering a number")

while True:
    try:
        transportation = float(input("what is your monthly transportation?:"))
        break
    except:
        print("enter a number!!!! rebukes you for not entering a number")

percentage1 = rent/income * 100
percentage2 = utilities/income * 100
percentage3 = groceries/income * 100
percentage4 = transportation/income * 100
savings = income / 10

print(f"your rent is ${rent} a month, which is {percentage1:.2f}% of your income.")
print(f"your utilities are ${utilities} a month, which is {percentage2:.2f}% of your income.")
print(f"your groceries are ${groceries} a month, which is {percentage3:.2f}% of your income.")
print(f"your transportation is ${transportation} a month, which is {percentage4:.2f}% of your income.")
print(f"you should put ${savings:.2f} into your savings every month.")

total = income - rent - utilities - groceries - transportation - savings
print(f"you have ${total:.2f} of spending money left over at the end of every month. yayy")

#this is actually really fun when i know what im doing
#yay
