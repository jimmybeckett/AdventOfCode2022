import itertools


def advance(blizzards, height, width):
    new_blizzards = {}
    for (r, c), bs in blizzards.items():
        for b in bs:
            match b:
                case '>':
                    new_r, new_c = r, c + 1
                    if new_c == width - 1:
                        new_c = 1
                case '<':
                    new_r, new_c = r, c - 1
                    if new_c == 0:
                        new_c = width - 2
                case '^':
                    new_r, new_c = r - 1, c
                    if new_r == 0:
                        new_r = height - 2
                case 'v':
                    new_r, new_c = r + 1, c
                    if new_r == height - 1:
                        new_r = 1
            new_blizzards.setdefault((new_r, new_c), set()).add(b)
    return new_blizzards


def traversal_time(blizzards, height, width, start, end):
    positions = {start}
    for minute in itertools.count(start=1):
        new_positions = set()
        blizzards = advance(blizzards, height, width)
        for r, c in positions:
            for new_r, new_c in [(r, c), (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (new_r, new_c) not in blizzards and (
                        (new_r, new_c) == start or (new_r, new_c) == end or (
                        new_r in range(1, height - 1) and new_c in range(1, width - 1))):
                    new_positions.add((new_r, new_c))
        if end in new_positions:
            return minute, blizzards
        positions = new_positions


def part_1(blizzards, height, width):
    start = (0, 1)
    end = (height - 1, width - 2)
    minutes, _ = traversal_time(blizzards, height, width, start, end)
    return minutes


def part_2(blizzards, height, width):
    start = (0, 1)
    end = (height - 1, width - 2)
    minutes1, blizzards1 = traversal_time(blizzards, height, width, start, end)
    minutes2, blizzards2 = traversal_time(blizzards1, height, width, end, start)
    minutes3, _ = traversal_time(blizzards2, height, width, start, end)
    return minutes1 + minutes2 + minutes3


with open('scratch.txt') as f:
    width = height = 0
    blizzards = {}
    for r, line in enumerate(f):
        height = max(height, r + 1)
        for c, char in enumerate(line):
            width = max(width, c)
            if char != '.' and char != '#' and char != '\n':
                blizzards[(r, c)] = char
    # print(blizzards, height, width)
    print(part_1(blizzards, height, width))
    print(part_2(blizzards, height, width))
