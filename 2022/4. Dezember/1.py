import re
with open('2022/4. Dezember/pairs.txt') as f:
    pair_list = [list(map(int, re.findall('[0-9]+', item))) for item in f.read().split('\n')]

counter = 0

for item in pair_list:
    if item[0] <= item[2] and item[1] >= item[3]:
        counter += 1
    elif item[0] >= item[2] and item[1] <= item[3]:
        counter += 1

print(f"{counter} pairs contain each other")