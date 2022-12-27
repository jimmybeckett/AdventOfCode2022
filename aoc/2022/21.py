import operator
import re
from polynomial import Polynomial


def part_1(rel_monkeys, const_monkeys):
    def helper(m):
        if m in const_monkeys:
            return const_monkeys[m]
        m1, op, m2 = rel_monkeys[m]
        return op(helper(m1), helper(m2))

    return helper('root')


def part_2(rel_monkeys, const_monkeys):
    def helper(m):
        if m == 'humn':
            return Polynomial(1, 0)
        if m in const_monkeys:
            return Polynomial(const_monkeys[m])
        m1, op, m2 = rel_monkeys[m]
        return op(helper(m1), helper(m2))

    left, _, right = rel_monkeys['root']
    poly = helper(left) - helper(right)
    # Newton's method
    x = 0
    for _ in range(10):
        x = x - poly.calculate(x) / poly.derivative.calculate(x)
    return round(x)


with open('scratch.txt') as f:
    ops = {'*': operator.mul, '+': operator.add, '-': operator.sub, '/': operator.floordiv}
    rel_monkeys, const_monkeys = {}, {}
    for line in f:
        if match := re.match(r'([a-z]{4}): (\d+)', line):
            const_monkeys[match.group(1)] = int(match.group(2))
        else:
            match = re.match(r'([a-z]{4}): ([a-z]{4}) (.) ([a-z]{4})', line)
            rel_monkeys[match.group(1)] = (match.group(2), ops[match.group(3)], match.group(4))
    print(part_1(rel_monkeys, const_monkeys))
    print(part_2(rel_monkeys, const_monkeys))
