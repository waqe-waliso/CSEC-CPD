width=0
a= [int(x) for x in input().split()]
height= [int(x) for x in input().split()]
for i in range (a[0]):
    if height[i]<=a[1]:
        width+=1
    else:
        width+=2
print(width)
