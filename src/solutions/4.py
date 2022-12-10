import re


def overlap_1(a, b, c, d):
    return (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d)


def overlap_2(a, b, c, d):
    return a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d


def solution(overlap):
    with open("../../data/4.txt") as f:
        prog = re.compile("(\\d+)-(\\d+),(\\d+)-(\\d+)")
        count = 0
        for line in f:
            nums = [int(n) for n in prog.match(line).groups()]
            if overlap(*sorted(nums[:2]), *sorted(nums[2:])):
                count += 1
        return count


print(solution(overlap_1))
print(solution(overlap_2))
