from dataclasses import dataclass
import re

BORDER = 100_000

@dataclass
class item:
    name: str
    size: int # size or -1 for folder

with open('2022/7. Dezember/instructions.txt') as f:
    instructions = f.read().split('\n')



file_system = {}
current_folder_list = []
current_folder_name = '/'

for instruction in instructions:
    if instruction.startswith('$ cd'):
        # The reason because it fails: Multiple folders with same names‚
        if current_folder_name in file_system.keys():
            print('overwrite')
        file_system[current_folder_name] = current_folder_list
        items = re.findall('[a-z]+|[.]+|/', instruction)

        # .. is no folder
        if items[1] == '..':
            continue

        current_folder_name = items[1]
        current_folder_list = []
    elif instruction.startswith('$ ls'):
        continue
    else:
        items = re.findall('[a-z|.]+|[0-9]+', instruction)
        
        if items[0] == 'dir':
            current_folder_list.append(item(name=items[1], size=-1))
        else:
            current_folder_list.append(item(name=items[1], size=int(items[0])))
file_system [current_folder_name] = current_folder_list


def get_size(folder):
    folder_size = 0
      
    for _item in file_system[folder]:
        if _item.size == -1:
            folder_size += get_size(_item.name)
        else:
            folder_size += _item.size
    return folder_size


sum_of_folders_under_border = 0
# sizes = []
for key in file_system.keys():
    size = get_size(key)
    # sizes.append(size)
    if size <= BORDER:
        sum_of_folders_under_border += size

        

# print(sizes)
print(f"The sum is {sum_of_folders_under_border}")
# falsch:
# 1587614
# 1683051
