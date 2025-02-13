y, w = map(int, input().split())
 
min_roll = max(y, w)
favorable_outcomes = 7 - min_roll
total_outcomes = 6
 
gcd_value = 1
for i in range(1, min(favorable_outcomes, total_outcomes) + 1):
    if favorable_outcomes % i == 0 and total_outcomes % i == 0:
        gcd_value = i
 
numerator = favorable_outcomes // gcd_value
denominator = total_outcomes // gcd_value
 
print(f"{numerator}/{denominator}")
