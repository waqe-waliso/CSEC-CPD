s = input()
t = input()
 
position = 0
 
for instruction in t:
    if position < len(s) and s[position] == instruction:
        position += 1
 
print(position + 1)
