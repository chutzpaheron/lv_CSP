# LV, period 7, nesting loops

count = 2

for num in range(1,21):
    if num % 15 == 0:
        print("Hi")
    elif num % 3 == 0:
        print("Hello")
    elif num % 5 == 0:
        print("H")
    else:
        print(num)

while count <= 20:
    print(count)
    count += 2

#nesting works like a russian doll
#everything must be done in order #KEEP TRACK OF TABS
#colon means tab next line

insects = ["assassin bug", "bindweed bee", "blue mud dauber", "blue skimmer", "cecropia moth", "darkling beetle"]
count = 1
while count < len(insects):
    print(f"{count}.{insects[count-1]}")
    count += 1
else:
    print("NO INSECTS")
