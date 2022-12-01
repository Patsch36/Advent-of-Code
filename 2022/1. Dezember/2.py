with open('1. Dezember/calories.txt') as f:
    calorie_list = f.read().split("\n\n")


sum_list = []
elve_index = 0
for index, item in enumerate(calorie_list):
    sum_list.append(sum(list(map(int, item.split("\n")))))

cals = 0
for i in range(3):
    maxval = max(sum_list)
    sum_list.remove(maxval)
    cals += maxval

print(f"The top 3 elves having {cals} calories")