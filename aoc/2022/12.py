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

    starting_locations = [(r, c) for r in range(len(height_map)) for c in range(len(height_map[0])) if
                          height_map[r][c] in starting_chars]
    nodes = {start: 0 for start in starting_locations}
    for num_moves in itertools.count(start=1):
        for r, c in list(nodes.keys()):
            for new_r, new_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= new_r < len(height_map) and 0 <= new_c < len(height_map[0]) and height(
                        height_map[new_r][new_c]) <= height(height_map[r][c]) + 1:
                    nodes.setdefault((new_r, new_c), num_moves)
                    if height_map[new_r][new_c] == 'E':
                        return num_moves


print(moves('S'))  # Part 1
print(moves('Sa'))  # Part 2
