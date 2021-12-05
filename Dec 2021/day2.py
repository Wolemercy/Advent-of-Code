from typing import List

def get_input(file: str) -> List[str]:
    data = []
    with open(file) as f:
        for line in f.readlines():
            data.append((line.strip()))
    return data

def dive_one(data: List[str]) -> int:
    horizontal = vertical = 0
    for position in data:
        if position[0] == 'f':
            horizontal += int(position[-1])
        elif position[0] == 'd':
            vertical += int(position[-1])
        else:
            vertical += -1 * int(position[-1])
    print(f'Part 1: {horizontal * vertical}')

def dive_two(data: List[str]) -> int:
    aim = horizontal = vertical = 0
    for position in data:
        if position[0] == 'f':
            horizontal += int(position[-1])
            vertical += aim * int(position[-1])
        elif position[0] == 'd':
            aim += int(position[-1])        
        else:
            aim += -1 * int(position[-1])
    print(f'Part 2: {horizontal * vertical}')


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    dive_one(puzzle_input)
    dive_two(puzzle_input)
