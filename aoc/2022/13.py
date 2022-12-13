import functools

import utils


def paired_packets():
    with utils.get_input(2022, 13) as f:
        while line := f.readline():
            yield eval(line), eval(f.readline())
            f.readline()  # skip newline


def is_ordered(left, right):
    for l, r in zip(left, right):
        if type(l) is int and type(r) is int:
            ordered = None if l == r else l < r
        elif type(l) is list and type(r) is list:
            ordered = is_ordered(l, r)
        elif type(l) is list:
            assert type(r) is int
            ordered = is_ordered(l, [r])
        else:
            assert type(l) is int and type(r) is list
            ordered = is_ordered([l], r)
        if ordered is not None:
            return ordered

    return None if len(left) == len(right) else len(left) < len(right)


def bubble_sort(lst, comparator):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if not comparator(lst[j], lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def part_1():
    return sum(idx for idx, (left, right) in enumerate(paired_packets(), start=1) if is_ordered(left, right))


def part_2():
    dividers = [[[2]], [[6]]]
    packets = dividers + [packet for pair in paired_packets() for packet in pair]
    bubble_sort(packets, is_ordered)
    return functools.reduce(lambda i, j: (i + 1) * (j + 1), [packets.index(divider) for divider in dividers])


print(part_1())
print(part_2())
