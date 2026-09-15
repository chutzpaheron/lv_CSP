# LV, period 7, hello user

while True:
    answer = input("hello, Would you like to be spared:").strip().upper()
    if answer.isnumeric():
     print("no fooling around.")
    elif " " in answer:
     print("give a SIMPLE YES OR NO!!!")
    else:
     break
print(f"ok, {answer} shall be your fate!!")
