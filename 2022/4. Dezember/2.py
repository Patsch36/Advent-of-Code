import re
with open('2022/4. Dezember/pairs.txt') as f:
    pair_list = [list(map(int, re.findall('[0-9]+', item))) for item in f.read().split('\n')]

def contains(number, lower_range, upper_range):
    return number in range(lower_range, upper_range + 1)

counter = 0

for item in pair_list:
    # check if one border is in the other interval
    if contains(item[0], item[2], item[3]):
        counter += 1
    elif contains(item[1], item[2], item[3]): 
        counter += 1
    elif contains(item[2], item[0], item[1]): 
        counter += 1
    elif contains(item[3], item[0], item[1]): 
        counter += 1

print(f"{counter} pairs overlap each other")