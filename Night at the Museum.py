exhibit_name = input()
 
current_letter = 'a'
total_rotations = 0
 
for target_letter in exhibit_name:
    distance = abs(ord(target_letter) - ord(current_letter))
    total_rotations += min(distance, 26 - distance)
    current_letter = target_letter
 
print(total_rotations)
