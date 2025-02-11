x = input()
u = 0
l = 0

for k in x:
    if k.isupper():
        u += 1
    elif k.islower():
        l += 1

if l >= u:
    print(x.lower())
else:
    print(x.upper())
