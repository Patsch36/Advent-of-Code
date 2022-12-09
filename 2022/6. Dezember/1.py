with open('2022/6. Dezember/puzzle.txt') as f:
    datastream = f.read()

for i in range(len(datastream)-4):
    characters = list(datastream[i:i+4])
    if len(set(characters)) == len(characters):
        print(f"There must be {i+4} characters processed before the first marker is set")
        break