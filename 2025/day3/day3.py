#
# Advent of Code no.3
# December 3, 2025
# Sam W.
#

def find_max_joltage(bank):
    max_joltage = 0

    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)

    return max_joltage

def find_max_joltage_pt2(bank):
    batts_to_skip = len(bank) - 12

    batteries = [(digit, i) for i, digit in enumerate(bank)]

    sorted_batteries = sorted(batteries, key=lambda x: (x[0], -x[1]))

    batteries_to_keep = sorted_batteries[batts_to_skip:]
    batteries_to_keep.sort(key=lambda x: x[1])

    joltage_str = ''.join(digit for digit, _ in batteries_to_keep)
    return int(joltage_str)


def main():
    total_joltage1 = 0
    
    with open("input.text","r") as f:
        for line in f:
            bank = line.strip()
            if bank:
                max_joltage = find_max_joltage(bank)
                total_joltage1 += max_joltage
    
    print("Total Maximum Joltage (p1): ", total_joltage1)

    total_joltage2 = 0

    with open("input.text", "r") as f:
        for line in f:
            bank2 = line.strip()
            if bank2:
                max_joltage = find_max_joltage_pt2(bank2)
                total_joltage2 += max_joltage

    print("Total Maximum Joltage (p2): ", total_joltage2)

if __name__ == "__main__":
    main()