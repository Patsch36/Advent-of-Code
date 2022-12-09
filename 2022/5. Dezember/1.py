import re
from collections import deque
import pandas as pd

' Get puzzle'
with open("2022/5. Dezember/puzzle.txt") as f:
    puzzle = f.read().split("\n\n")

# Get number of stacks
stack_lines = puzzle[0].split("\n")
stacks = list(map(int, re.findall("[0-9]+", stack_lines[-1])))
amount_of_stacks = len(stacks)

# Create stacks
stacks = []
for i in range(amount_of_stacks):
    stacks.append([])

# Check each stack for items -> Fill stacks
for index in range(amount_of_stacks):
    for line in stack_lines[0:-1]:
        if line[1+4*index] != ' ':
            stacks[index].append(line[1+4*index])
for stack in stacks:
    stack.reverse()

# Build instruction list
movement_list = pd.DataFrame(columns=['amount_of_crates', 'start_stack', 'end_stack'])
for instruction in puzzle[1].split("\n"):
    newline = list(map(int, re.findall('[0-9]+', instruction)))
    movement_list.loc[len(movement_list)] = newline
        
# Do instructions
for row in range(0, len(movement_list)):
    amount = movement_list.iloc[row]['amount_of_crates']
    for i in range(0, amount):
        end_stack = movement_list.iloc[row]['end_stack'] - 1
        start_stack = movement_list.iloc[row]['start_stack'] - 1
        stacks[end_stack].append(stacks[start_stack].pop())

# Build resolution
res = ""
for stack in stacks:
    res += stack[-1]

print(f"The top crates are {res}")
