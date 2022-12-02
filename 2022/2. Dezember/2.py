score_list = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 0,
    'Y': 3,
    'Z': 6
}

def get_choice(adversary: str, result:str) -> str:
    if result == 'X':
        return chr( ( ( ord(adversary) - 66 ) %3 ) + 65 )
    elif result == 'Y':
        return adversary
    else:
        return chr( ( ( ord(adversary) - 64 ) %3 ) + 65 )

with open('2022/2. Dezember/guide.txt') as f:
    text = [item.split(' ') for item in f.read().split('\n')]

score = 0
for item in text:
    score += score_list[item[1]] + score_list[get_choice(item[0], item[1])]

print(f"Your score is {score} points")