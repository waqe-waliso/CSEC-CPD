wire = int(input())
birds = [int(x) for x in input().split()]
shoots = int(input())

for i in range(shoots):

    x, y = map(int, input().split())
    x -= 1
    if x > 0:
        birds[x - 1] += y - 1
    if x < wire - 1:
        birds[x + 1] += birds[x] - y
    birds[x] = 0

for bird in birds:
    print(bird)
