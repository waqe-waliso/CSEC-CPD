s1, s2, s3, s4 = map(int, input().split())
 
unique_colors = len({s1, s2, s3, s4})
 
print(4 - unique_colors)
