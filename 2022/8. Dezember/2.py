from math import prod

with open('2022/8. Dezember/map.txt') as f:
    map_lines = f.read().split('\n')
tree_map = []
for line in map_lines:
    tree_map.append([int(char) for char in line])


# Edge trees are always visible
visible_trees = 2 * (len(tree_map) + (len(tree_map[0]) - 2))

count_tree = True
highscore = 0
highscore_tree = (0, 0)
for y in range(1, len(tree_map)-1):
    for x in range(1, len(tree_map[y])-1):
        view = [0,0,0,0]
        score = 0
        
        # Check upper trees
        for y_o in range(y - 1, -1, -1):
            view[0] += 1
            if tree_map[y_o][x] >= tree_map[y][x]:
                break
                

        # Check left trees
        for x_o in range(x - 1, -1, -1):
            view[1] += 1
            if tree_map[y][x_o] >= tree_map[y][x]:
                break

        # Check lower trees
        for y_o in range(y + 1, len(tree_map)):
            view[2] += 1
            if tree_map[y_o][x] >= tree_map[y][x]:
                break

        # Check right trees
        for x_o in range(x + 1, len(tree_map[y])):
            view[3] += 1
            if tree_map[y][x_o] >= tree_map[y][x]:
                break

        score = prod(view)
        if score > highscore:
            highscore = score
            highscore_tree = (x, y)




print(f"There biggest view is {highscore} ")
