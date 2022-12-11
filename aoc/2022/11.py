import operator
import re
from collections import namedtuple

import utils


def operation_fn(n, op, m):
    def val(var, old):
        return old if var == "old" else int(var)

    op_fn = operator.mul if op == "*" else operator.add
    return lambda old: op_fn(val(n, old), val(m, old))


def test_fn(d, t, f):
    return lambda worry_level: int(t if worry_level % int(d) == 0 else f)


def get_ints(string):
    return list(map(int, re.findall(r"(\d+)", string)))


def get_monkeys():
    with utils.get_input(2022, 11) as f:
        Monkey = namedtuple("Monkey", "items operation test")
        monkeys = []
        divisor_product = 1
        while f.readline():
            starting_items = get_ints(f.readline())
            operation = operation_fn(*re.match(r".*(old|\d+) (.) (old|\d+)", f.readline()).groups())
            divisor = get_ints(f.readline())[0]
            divisor_product *= divisor
            test = test_fn(divisor, get_ints(f.readline())[0], get_ints(f.readline())[0])
            f.readline()
            monkeys.append(Monkey(starting_items, operation, test))
    return monkeys, divisor_product


def monkey_business(monkeys, divisor_product, rounds, relief_divisor):
    num_items_inspected = [0] * len(monkeys)
    for r in range(rounds):
        for m, monkey in enumerate(monkeys):
            num_items_inspected[m] += len(monkey.items)
            for _ in range(len(monkey.items)):
                monkey.items[0] = monkey.operation(monkey.items[0]) % divisor_product
                monkey.items[0] //= relief_divisor
                monkeys[monkey.test(monkey.items[0])].items.append(monkey.items.pop(0))
    num_items_inspected.sort()
    return num_items_inspected[-1] * num_items_inspected[-2]


x = get_monkeys()
print(monkey_business(*x, 20, 3))  # Part 1
print(monkey_business(*x, 10000, 1))  # Part 2
