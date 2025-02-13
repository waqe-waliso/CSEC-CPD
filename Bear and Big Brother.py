a=[int(x) for x in input().split()]
n=0
while a[1]>=a[0]:
    a[0]*=3
    a[1]*=2
    n+=1
print(n)
