matrix = [[int(x) for x in input().split()]for i in range(5)]

for i in range(5):
    
    if 1 in matrix[i]:
        index_one = matrix[i].index(1)
        print(abs(2-i)+abs(2-index_one)) 
