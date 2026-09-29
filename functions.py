# LV, period 7, functions and code structure

def stupid(money):
    while True:
        try:
            amount = float(input(f"what is your monthly {money}?:"))
            return amount #continues as usual
        except:
            print("NOT A NUMBER")

income = stupid("income") #parameter gets info from the user (income)
rent = stupid("rent") #use the same function all four times
utilities = stupid("utilities")
groceries = stupid("groceries")
transportation = stupid("transportation") #1
savings = income / 10

def calc_percent(income, bills): #DEF means define, it is how you start EVERY FUNCTION #then, name function, use snake_case
    #new line. after function you put parentheses, inside these are PARAMETERS #pieces of info needed for the function to work
    #put colon, then indent
    #when using equations use parameter names as values
    #RETURN is a print with no user output, it is sent to code
    return round(bills / income * 100) #2

print(f"your rent is ${rent:.2f} which is {calc_percent(income, rent)}% of your income") #{calc_percent(income, rent)} is the function call
#this is what activates the function
#ARGUMENT is the value of the variable when function is run #bill = rent, but second time over bill = utilities
print(f"your utilities are ${utilities:.2f} which is {calc_percent(income, utilities)}% of your income")
print(f"your groceries are ${groceries:.2f} which is {calc_percent(income, groceries)}% of your income")
print(f"transportation is ${transportation:.2f} which is {calc_percent(income, transportation)}% of your income")
print(f"you should save ${savings:.2f} monthly, which is {calc_percent(income, savings)}% of your income")
print(f"you have ${income - rent - utilities - groceries - transportation - savings:.2f} left over every month") #3

#first, write ALL your variables
#second write any functions
#third are outputs


