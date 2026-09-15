# LV, period 7, fixing user inputs

while True: # code repeats  until the break
 color = input("tell me a color: ").strip().capitalize() # strip removes any spaces user inserted # upper() makes it uppercase, lower() lowercase, etc # title caps first letter of every word
 if color.isnumeric(): # checks if a specific condition is true (if there are numbers typed in)
        print("no numbers")
 elif " " in color: # only occurs when the if is false
     print("one word")
 else:
     break # ends the loop

print(f"we painted the walls {color}!!")