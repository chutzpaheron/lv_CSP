# LV, period 7, numbers

for num in range(1,21):
    if num % 2 == 0:
        if num % 5 == 0:
            print(f"{num} is even and divisible by 5")
        else: 
            print(f"{num} is even and indivisible by 5") 
    elif num % 5 == 0:
        if num % 5 == 0:
                print(f"{num} is odd and divisible by 5")
        else:
            print(f"{num} is even and indivisible by 5")
    else:
        print(f"{num} is odd and indivisible by 5")