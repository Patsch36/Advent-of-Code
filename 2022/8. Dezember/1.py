with open('2022/8. Dezember/map.txt') as f:
    map_lines = f.read().split('\n')
tree_map = []
for line in map_lines:
    tree_map.append([int(char) for char in line])


# Edge trees are always visible
visible_trees = 2 * (len(tree_map) + (len(tree_map[0]) - 2))

count_tree = True
for y in range(1, len(tree_map) - 1):
    for x in range(1, len(tree_map[y]) - 1):
        count_tree = True
        
        # Check upper trees
        for y_o in range(y - 1, -1, -1):
            if tree_map[y_o][x] >= tree_map[y][x]:
                count_tree = False
                break

        if count_tree:
            visible_trees += 1
            continue
        count_tree = True

        # Check left trees
        for x_o in range(x - 1, -1, -1):
            if tree_map[y][x_o] >= tree_map[y][x]:
                count_tree = False
                break
        
        if count_tree:
            visible_trees += 1
            continue
        count_tree = True

        # Check lower trees
        for y_o in range(y + 1, len(tree_map)):
            if tree_map[y_o][x] >= tree_map[y][x]:
                count_tree = False
                break

        if count_tree:
            visible_trees += 1
            continue
        count_tree = True

        # Check right trees
        for x_o in range(x + 1, len(tree_map[y])):
            if tree_map[y][x_o] >= tree_map[y][x]:
                count_tree = False
                break

        if count_tree:
            visible_trees += 1
            continue


print(f"There are {visible_trees} visible trees")
