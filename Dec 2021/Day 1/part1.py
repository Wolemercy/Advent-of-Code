inputFile = open('input.txt', 'r')
data = list(map(int, inputFile.read().splitlines()))

def sonar_sweep(measurements: list) -> int:
    prev = measurements[0]

    count = 0
    for measure in measurements:
        if measure > prev:
            count += 1
        prev = measure

    return count

res = sonar_sweep(data)
print(res)
