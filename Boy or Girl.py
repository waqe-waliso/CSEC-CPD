x = input()
y = ""
for k in x:
    if k not in y:
        y += k
if len(y) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

    
