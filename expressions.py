# LV, period 7, integers and float points, expressions notes
# gdbysgbuyijehaughufrjghiurghdshjgfhghjfhjgdfyergfysukjgfdhjnmbvgfbvuygrgvuysedhiuersh
# integers are just numbers, they ONLY hold whole numbers

people = 24
cars = 50
computers = 29
sentience = 0

# floats- pi, temperature, stuff that may come in decimals (3.14, 78.3, 2.97)

pi = 3.141596
temp = 78.3
cost = 2.97

# + for addition, - (little one) for subtraction etc
# * for multiplying, / is division, ** for exponents, % (mod) for remainders, // integer division
# arithmetic operators ^
# = means setting a variable, use expressions instead

print(f"the result of 18/4 is {18/4}")
print(f"the result of 23%5 is {23%5}")
print(f"the result of 18/4 is {18/4}, or {18//4} with a remainder of {18%4}")

# modulo expression only gives the remainder
# pemdas in coding is PARENTHESES, EXPONENTS, MULTIPLICATION MODULO DIVISION (INTEGERS), ADDITION AND SUBTRACTION

average = (85+23+69+90+33)/5
print(f"the average of Those Numbers is {average}")

grades = [85, 99, 78, 92, 65, 92, 90] # i assume [brackets] are to start a list?
students = len(grades)
average = sum(grades)/students
print(f"the average grade of Those Students is {int(average)}")

# int > integer, float > decimals, str > string
# inputs always give you a string, you CANNOT do math with a string, must be converted into a float or integer
# converting strings

price = float(input("hello, how much did this cost?:"))
tax = 0.0485
sales_tax = float(price) * tax
total = float(price) + sales_tax
print(F"the total cost is {total}")
# oh my god im not gonna remember any of this am i

# float(input()) converts it into float (decimals)