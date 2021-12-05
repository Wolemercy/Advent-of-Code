inputFile = open('input.txt', 'r')
data = list(map(int, inputFile.read().splitlines()))

# Part 1
def sonar_sweep(measurements: list) -> int:
    prev = measurements[0]

    count = 0
    for measure in measurements:
        if measure > prev:
            count += 1
        prev = measure

    return count

print(f'Number of increments are {sonar_sweep(data)}')

# Part 2
def sonar_sweep2(measurements: list) -> int:
    prev = sum(measurements[0:3])

    count = 0
    for i in range(1, len(measurements) - 2):
        curr = prev - measurements[i - 1] + measurements[i + 2]

        if curr > prev:
            count += 1

        prev = curr

    return count

print(f'Number of sums larger than previous are {sonar_sweep2(data)}')
