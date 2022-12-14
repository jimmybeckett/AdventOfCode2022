import itertools
import re

import utils


def chunk(iterable, n):
    itr = iter(iterable)
    return [*zip(*[itr]*n)]


def get_paths():
    paths = []
    with utils.get_scratch_input() as f:
        for line in f:
            nums = list(map(int, re.findall(r'\d+', line)))
            paths.append(chunk(nums, 2))
    return paths


def get_cave(has_floor=False):
    paths = get_paths()
    height, width = bounds(paths)
    if has_floor:
        height += 2
        # width = max(width, 2 * height - 1)
        width = 1000
    cave = [['.'] * width for _ in range(height)]
    for path in paths:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            for r in range(min(y1, y2), max(y1, y2) + 1):
                for c in range(min(x1, x2), max(x1, x2) + 1):
                    cave[r][c] = '#'
    if has_floor:
        for c in range(width):
            cave[-1][c] = '#'
    return cave


def print_sample_cave(cave):
    for row in cave[:10]:
        print(row[494:504])


def bounds(paths):
    xs, ys = zip(*((x, y) for path in paths for x, y in path))
    return max(ys) + 1, max(xs) + 1


def part_1():
    cave = get_cave()
    height, width = len(cave), len(cave[0])
    for sand_unit in itertools.count():
        r, c = 0, 500  # r, c = y, x
        while True:
            if r >= height - 1 or c <= 0 or c >= width - 1:
                return sand_unit

            if cave[r + 1][c] == '.':
                r += 1
            elif cave[r + 1][c - 1] == '.':
                r += 1
                c -= 1
            elif cave[r + 1][c + 1] == '.':
                r += 1
                c += 1
            else:
                cave[r][c] = 'o'
                break


def part_2():
    cave = get_cave(has_floor=True)
    for sand_unit in itertools.count():
        r, c = 0, 500  # r, c = y, x
        while True:
            if cave[r + 1][c] == '.':
                r += 1
            elif cave[r + 1][c - 1] == '.':
                r += 1
                c -= 1
            elif cave[r + 1][c + 1] == '.':
                r += 1
                c += 1
            else:
                cave[r][c] = 'o'
                if r == 0 and c == 500:
                    return sand_unit + 1
                break


print(part_1())
print(part_2())