import string 

with open('2022/3. Dezember/rucksacks.txt') as f:
    rucksacklist = f.read().split('\n')

def get_priority(char):
    if str.islower(char):
        return string.ascii_lowercase.index(char) + 1
    else:
        return string.ascii_uppercase.index(char) + 27


sum = 0
for rucksack in rucksacklist:
    delimitter = int(len(rucksack)/2)

    for character in rucksack[0:delimitter]:
        if character in rucksack[delimitter:len(rucksack)]:
            sum += get_priority(character)
            break

print(f"You're overall sum is {sum}.")