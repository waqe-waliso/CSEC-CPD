x = int(input())
y = []
w = []
c = 1
for i in range(x):
    z = input()
    y.append(z)
for i in range(1, len(y)):
    if y[i] == y[i-1]:
        c += 1
    else:
        w.append(c)
        c = 1 
w.append(c)
print(len(w))
