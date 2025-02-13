a1, a2, a3, a4 = map(int, input().split())
s = input().strip()
 
calories = 0
 
for char in s:
    calories += [a1, a2, a3, a4][int(char) - 1]
 
print(calories)
