problems=int(input())
n=0
for i in range(problems):
    sure=input()
    a=sure.count('1')
    if a>1:
        n+=1
    else:
        continue
print(n)
