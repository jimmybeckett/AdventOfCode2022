import collections
import itertools

import utils


def moves(starting_chars):
    def height(c):
        match c:
            case 'S':
                return height('a')
            case 'E':
                return height('z')
            case _:
                return ord(c)

    with utils.get_input(2022, 12) as f:
        height_map = [list(line.strip()) for line in f]

    rows, cols = len(height_map), len(height_map[0])
    starting_locations = [(r, c) for r in range(rows) for c in range(cols) if height_map[r][c] in starting_chars]
    q = collections.deque(starting_locations)
    visited = set(q)
    for num_moves in itertools.count(start=1):
        for _ in range(len(q)):
            r, c = q.popleft()
            for new_r, new_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if new_r in range(rows) and new_c in range(cols) and height(height_map[new_r][new_c]) <= height(
                        height_map[r][c]) + 1 and (new_r, new_c) not in visited:
                    if height_map[new_r][new_c] == 'E':
                        return num_moves
                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))


print(moves('S'))  # Part 1
print(moves('Sa'))  # Part 2
