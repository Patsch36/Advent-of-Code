from dataclasses import dataclass
import re

BORDER = 100_000

# Build up a tree
@dataclass
class Node:
    name: str
    parent: str
    size: int
    childs: list

# Write recursive function for summing up all files in the node
def sum_tree(node, nodes):
    if not node.childs:
        return node.size
    for child in node.childs:
        node.size += sum_tree(nodes[child], nodes)
    return node.size

# Get instructions
with open('2022/7. Dezember/instructions.txt') as f:
    instructions = f.read().split('\n')

# Creating root node
node = Node(name=' ', parent=' ', size=0, childs=[])
nodes = {' ': node}

for instruction in instructions:
    items = re.findall('[a-z|.|/]+|[0-9]+', instruction)
    # Because ffrom files only the overall size matters, 
    # save the size of all files in nodes' size and don't store them
    if items[0].isdigit():
        node.size += int(items[0])
    elif items[0] == 'cd':
        dir_name = items[1]

        # Getting one level back
        if dir_name == '..':
            node = nodes[node.parent]
        # Getting one level depper in system
        else:
            # Creating child and add to child list
            child = node.name + '/' + dir_name
            node.childs.append(child)

            if child in nodes:
                node = nodes[child]
            else:
                node = Node(name=child, parent=node.name, size=0, childs=[])
                nodes[child] = node

sum_tree(nodes[' '], nodes)
sum_ = sum([node.size for node in nodes.values() if node.size <= BORDER])

print(f"The sum of all files lower than {BORDER} is {sum_}")
