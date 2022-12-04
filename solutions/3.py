from functools import reduce
from itertools import chain


def group_compartments(f, split_line, num_lines):
    while line := f.readline():
        yield split_line(line) + list(chain(*(split_line(f.readline()) for _ in range(num_lines - 1))))


def intersection(sets):
    return reduce(lambda x, y: z if (z := x & y) else y, sets, set())


def priority(item):
    return ord(item) - (96 if item.islower() else 38)


def priorities(split_line, num_lines):
    with open("../data/3.txt") as f:
        return sum(
            priority(intersection(map(set, compartments)).pop()) for compartments in
            group_compartments(f, split_line, num_lines))


print(priorities(lambda line: [line[:len(line) // 2], line[len(line) // 2:-1]], 1))  # Part 1
print(priorities(lambda line: [line.strip()], 3))  # Part 2
