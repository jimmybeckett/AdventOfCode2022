import functools

import utils


def paired_packets():
    with utils.get_input(2022, 13) as f:
        while line := f.readline():
            yield eval(line), eval(f.readline())
            f.readline()  # skip newline


# returns <0 if left < right, 0 if left == right, >0 if right > left
def is_ordered(left, right):
    for l, r in zip(left, right):
        match l, r:
            case int(), int():
                ordered = l - r
            case list(), list():
                ordered = is_ordered(l, r)
            case list(), int():
                ordered = is_ordered(l, [r])
            case int(), list():
                ordered = is_ordered([l], r)
        if ordered:
            return ordered

    return len(left) - len(right)


def part_1():
    return sum(idx for idx, (left, right) in enumerate(paired_packets(), start=1) if is_ordered(left, right) < 0)


def part_2():
    dividers = [[[2]], [[6]]]
    packets = dividers + [packet for pair in paired_packets() for packet in pair]
    packets.sort(key=functools.cmp_to_key(is_ordered))
    return functools.reduce(lambda i, j: (i + 1) * (j + 1), [packets.index(divider) for divider in dividers])


print(part_1())
print(part_2())
