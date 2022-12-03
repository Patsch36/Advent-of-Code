import string 

with open('2022/3. Dezember/rucksacks.txt') as f:
    rucksacklist = f.read().split('\n')

def get_priority(char):
    if str.islower(char):
        return string.ascii_lowercase.index(char) + 1
    else:
        return string.ascii_uppercase.index(char) + 27


sum = 0
for rucksacknumber in range(0, len(rucksacklist), 3):
    for character in rucksacklist[rucksacknumber]:
        if character in rucksacklist[rucksacknumber + 1] and character in rucksacklist[rucksacknumber + 2]:
            sum += get_priority(character)
            break

print(f"You're overall sum is {sum}.")