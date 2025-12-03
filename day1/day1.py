#
# Advent of Code no.1
# December 1, 2025
# Sam W.
#

from typing import List, Tuple

def hits_during_rotation_math(pos: int, turn: str, dist: int) -> int:
    """Math method: count k in 1..dist such that dial hits 0 during the rotation."""
    if dist <= 0:
        return 0
    if turn == "R":
        k0 = (-pos) % 100
    else:
        k0 = pos % 100
    if k0 == 0:
        k0 = 100
    if dist < k0:
        return 0
    return 1 + (dist - k0) // 100

def hits_during_rotation_bruteforce(pos: int, turn: str, dist: int) -> int:
    """Brute-force simulation of each click in the rotation."""
    count = 0
    p = pos
    if turn == "R":
        for _ in range(dist):
            p = (p + 1) % 100
            if p == 0:
                count += 1
    else:
        for _ in range(dist):
            p = (p - 1) % 100
            if p == 0:
                count += 1
    return count

def process(directions: List[str], verbose: bool = True) -> Tuple[int,int,int]:
    cur = 50
    part1 = 0
    part2_math = 0
    part2_brute = 0

    if verbose:
        print(f"{'#':>3}  {'instr':>6}  {'start':>5}  {'end':>5}  {'math_hits':>9}  {'bf_hits':>7}  {'end_is_0':>8}")
        print("-"*60)

    for i, raw in enumerate(directions, start=1):
        instr = raw.strip()
        if not instr:
            continue
        turn = instr[0].upper()
        dist = int(instr[1:])
        start = cur

        # math and brute counts for this rotation
        math_hits = hits_during_rotation_math(start, turn, dist)
        bf_hits = hits_during_rotation_bruteforce(start, turn, dist)

        # update cur
        if turn == "R":
            cur = (cur + dist) % 100
        else:
            cur = (cur - dist) % 100

        end = cur
        end_is_0 = 1 if end == 0 else 0

        part1 += end_is_0
        part2_math += math_hits
        part2_brute += bf_hits

        if verbose:
            mis = "!" if math_hits != bf_hits else ""
            print(f"{i:3d}  {instr:6s}  {start:5d}  {end:5d}  {math_hits:9d}  {bf_hits:7d}  {end_is_0:8d} {mis}")

    if verbose:
        print("-"*60)
        print(f"Totals -> Part1 (end-of-rotations): {part1}")
        print(f"Part2 math: {part2_math}")
        print(f"Part2 brute: {part2_brute}")
        if part2_math != part2_brute:
            print(">>> MISMATCH between math and brute! See lines marked '!' above.")
        else:
            print("Math and brute agree for all rotations.")

    return part1, part2_math, part2_brute

def run_example_and_input(filename: str = "input.text"):
    print("\n==========================================")
    try:
        with open(filename, "r") as f:
            lines = [ln.strip() for ln in f if ln.strip()]
    except FileNotFoundError:
        print(f"Error: couldn't open '{filename}'. Make sure filename is correct.")
        return
    
    process(lines, verbose=True)
    

if __name__ == "__main__":
    run_example_and_input("input.text")
