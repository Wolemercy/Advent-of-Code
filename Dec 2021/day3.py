from typing import List

def get_input(file: str) -> List[str]:
    data = []
    with open(file) as f:
        for line in f.readlines():
            data.append((line.strip()))
    return data

def bin_diagnostic_one(report: List[str]) -> int:
    bit_length = len(report[0])
    bits_seen = [[0, 0] for rep in range(bit_length)]

    for rep in report:
        for i in range(bit_length):
            if rep[i] == '0':
                bits_seen[i][0] += 1
            else:
                bits_seen[i][1] += 1

    gamma_bin = ''
    epsilon_bin = ''
    for bit in bits_seen:
        if bit[0] > bit[1]:
            gamma_bin += '0'
            epsilon_bin += '1'
        else:
            gamma_bin += '1'
            epsilon_bin += '0'

    gamma_dec = int(gamma_bin, 2)
    epsilon_dec = int(epsilon_bin, 2)

    print(f'Power consumption: { gamma_dec * epsilon_dec}')


def find_most_least(data: List[str], index: int) -> tuple:
    count = [0, 0]
    for d in data:
        if d[index] == '0':
            count[0] += 1     
        else:
            count[1] += 1    
    if count[0] > count[1]:
        return (0, 1)  
    else:
        return (1, 0)
        
def bin_diagnostic_two(report: List[str]) -> int:
    oxygen_gen = report
    co2_scrubber = report
    i = 0
    while len(oxygen_gen) > 1 or  len(co2_scrubber) > 1:
        # Oxygen Generator Rating
        if len(oxygen_gen) > 1:
            most, _ = find_most_least(oxygen_gen, i)
            oxygen_gen = list(filter(lambda x: x[i] == str(most), oxygen_gen))
        # CO2 Scrubber Rating
        if len(co2_scrubber) > 1:
            _, least = find_most_least(co2_scrubber, i)
            co2_scrubber = list(filter(lambda x: x[i] == str(least), co2_scrubber)) 
        i += 1

    oxygen_gen_rating = int(oxygen_gen[0], 2)
    co2_scrubber_rating = int(co2_scrubber[0], 2)

    print(f'Oxygen Generator: {oxygen_gen_rating}')
    print(f'CO2 Scrubber: {co2_scrubber_rating}')
    print(f'Life Support Rating: {oxygen_gen_rating * co2_scrubber_rating}')


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    bin_diagnostic_one(puzzle_input)
    bin_diagnostic_two(puzzle_input)
