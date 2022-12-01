

with open('1. Dezember/calories.txt') as f:
    calorie_list = f.read().split("\n\n")

calsum = 0
newsum = 0
elve_index = 0
for index, item in enumerate(calorie_list):
    newsum = sum(list(map(int, item.split("\n"))))
    if newsum > calsum:
        calsum = newsum
        elve_index = index

print(f"The elve with the most calories is elve numer {elve_index + 1} with {calsum} calories")
