number_of_cards = int(input())
cards = [int(x) for x in input().split()]
sereja = 0
dima = 0

while cards:
    
    if cards[0] > cards[-1]:
        sereja += cards.pop(0)
    else:
        sereja += cards.pop(-1)
    
    if cards:
        if cards[0] > cards[-1]:
            dima += cards.pop(0)
        else:
            dima += cards.pop(-1)

print(sereja, dima)
