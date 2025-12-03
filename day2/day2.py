# 
# Advent of Code no.2
# December 2, 2025
# Sam W.
#

def repeating_part1(n: int) -> bool:
    s = str(n)
    L = len(s)

    if L % 2 != 0: 
        return False
    
    half = L // 2

    return s[:half] == s[half:]

def repeating_part2(n: int) -> bool:
    s = str(n)
    L = len(s)

    for block_len in range(1, L // 2 + 1):
        if L % block_len != 0: continue

        block = s[:block_len]
        if block * (L // block_len) == s:
            return True
        
    return False


def main():
    total_p1 = 0
    total_p2 = 0

    with open("input.text","r") as f:
        line = f.read().strip()

    ranges = line.split(",")

    for r in ranges:
        if not r: continue

        lo, hi = map(int, r.split("-"))
        for n in range(lo, hi + 1):
            if repeating_part1(n): total_p1 += n

    print(f"Total (P1): {total_p1}")

    ######## Part 2 ########

    for j in ranges:
        if not j: continue

        lo2, hi2 = map(int, j.split("-"))
        for k in range(lo2, hi2 + 1):
            if repeating_part2(k): total_p2 += k

    print(f"Total (P2): {total_p2}")
        
if __name__ == "__main__":
    main()
