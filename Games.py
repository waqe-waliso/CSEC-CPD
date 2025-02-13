n = int(input())
teams = [tuple(map(int, input().split())) for _ in range(n)]

count = 0

for home_team in teams:
    for guest_team in teams:
        if home_team != guest_team and home_team[0] == guest_team[1]:
            count += 1

print(count)
