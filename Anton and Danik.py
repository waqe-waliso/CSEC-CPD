games = int(input())
winner = input()
A_wins = winner.count('A')
D_wins = winner.count('D')
if A_wins==D_wins:
    print("Friendship")
elif D_wins>A_wins:
    print("Danik")
else:
    print("Anton")
