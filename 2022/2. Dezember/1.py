score_list = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'loss': 0,
    'draw': 3,
    'win': 6
}

def get_win(choice: str, adversary: str) -> str:
    if ord(choice) - 23 == ord(adversary):
        return 'draw'
    
    if choice == 'X' and adversary == 'B':
        return 'loss'
    if choice == 'Y' and adversary == 'C':
        return 'loss'
    if choice == 'Z' and adversary == 'A':
        return 'loss'
    
    return 'win'

with open('2022/2. Dezember/guide.txt') as f:
    text = [item.split(' ') for item in f.read().split('\n')]

score = 0
for item in text:
    score += score_list[item[1]] + score_list[get_win(item[1], item[0])]

print(f"Your score is {score} points")