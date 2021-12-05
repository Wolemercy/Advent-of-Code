from typing import List

def get_input(file: str) -> List[int]:
    data = []
    with open(file) as f:
        for line in f.readlines():
            data.append(int(line.strip()))
    return data

# Part 1
def sonar_sweep_one(measurements: List[int]) -> int:
    prev = measurements[0]
    count = 0
    for measure in measurements:
        if measure > prev:
            count += 1
        prev = measure
    print(f'Number of increments are {count}')

# Part 2
def sonar_sweep_two(measurements: List[int]) -> int:
    prev = sum(measurements[0:3])
    count = 0
    for i in range(1, len(measurements) - 2):
        curr = prev - measurements[i - 1] + measurements[i + 2]
        if curr > prev:
            count += 1
        prev = curr
    print(f'Number of sums larger than previous are {count}')

if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    sonar_sweep_one(puzzle_input)
    sonar_sweep_two(puzzle_input)
