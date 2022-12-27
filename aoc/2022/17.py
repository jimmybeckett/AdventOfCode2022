# returns list of (r, c) rock positions
from collections import deque

from tqdm import tqdm


def rocks(n):
    rock_lst = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                [(2, 1), (1, 0), (1, 1), (1, 2), (0, 1)],
                [(2, 2), (1, 2), (0, 2), (0, 1), (0, 0)],
                [(0, 0), (1, 0), (2, 0), (3, 0)],
                [(0, 0), (0, 1), (1, 0), (1, 1)]]
    for i in range(n):
        yield rock_lst[i % len(rock_lst)]


with open('scratch.txt') as f:
    jets = list(f.readline().strip())


class Cave:
    def __init__(self):
        self.cave = [['.'] * 7 for _ in range(10000 * 13)]

    def is_rock(self, r, c):
        return self.cave[r][c] == '#'

    def set_rock(self, r, c):
        self.cave[r][c] = '#'


def height_increments(num_rocks):
    cave = [['.'] * 7 for _ in range(num_rocks * 4)]
    highest_spot = 0
    jet_idx = 0
    highest_incs = []
    for rock in rocks(num_rocks):
        rock = [(r + highest_spot + 3, c + 2) for r, c in rock]
        while True:
            jet = jets[jet_idx % len(jets)]
            jet_idx += 1
            # rock is pushed by jet
            if jet == '<':
                new_rock = [(r, c - 1) for r, c in rock]
            else:
                assert jet == '>'
                new_rock = [(r, c + 1) for r, c in rock]
            if all(c in range(7) and cave[r][c] == '.' for r, c in new_rock):
                rock = new_rock
            # rock falls
            new_rock = [(r - 1, c) for r, c in rock]
            if all(r >= 0 and cave[r][c] == '.' for r, c in new_rock):
                rock = new_rock
            else:
                break
        new_highest = max(highest_spot, max(r for r, _ in rock) + 1)
        highest_incs.append(new_highest - highest_spot)
        highest_spot = new_highest
        for r, c in rock:
            cave[r][c] = '#'
    return highest_incs


def detect_cycle(lst, min_length, max_length):
    for cycle_start in range(len(lst) // 2):
        for cycle_length in range(min_length, max_length + 1):
            if lst[cycle_start:cycle_start + cycle_length] == lst[
                                                              cycle_start + cycle_length:cycle_start + 2 * cycle_length]:
                return cycle_start, lst[cycle_start:cycle_start + cycle_length]


# 1, 3, 3, 4, 0, 1, 2, 3, 0, 1, 1, 3, 2, 2, 0, 0, 2, 3, 4, 0, 1, 2, 1, 2, 0, 1, 2, 1, 2, 0

def height(n, basis_length):
    incs = height_increments(basis_length)
    print('computed incs')
    cycle_start_idx, cycle = detect_cycle(incs, 15, basis_length // 2)
    print(f'detected cycle of length {len(cycle)}')
    header = incs[:cycle_start_idx]
    footer = cycle[:(n - len(header)) % len(cycle)]
    return sum(header) + sum(cycle) * (n - len(header) - len(footer)) // len(cycle) + sum(footer)


print(height(2022, 5000))  # Part 1
print(height(1000000000000, 5000))  # Part 2

