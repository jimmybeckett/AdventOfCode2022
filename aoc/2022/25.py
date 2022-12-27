base = 5


def snafu_2_decimal(s):
    n = 0
    for place, c in enumerate(reversed(s)):
        if c in ['0', '1', '2']:
            n += int(c) * base ** place
        elif c == '-':
            n += -1 * base ** place
        elif c == '=':
            n += -2 * base ** place
    return n


def decimal_2_snafu(n):
    b5 = []
    while n != 0:
        b5.insert(0, n % base)
        n //= base
    s_n = []
    for d in b5:
        s_n.append(d)
        i = len(s_n) - 1
        while s_n[i] in [3, 4, 5]:
            if s_n[i] == 3:
                s_n[i] = -2
            if s_n[i] == 4:
                s_n[i] = -1
            if s_n[i] == 5:
                s_n[i] = 0
            if i > 0:
                s_n[i - 1] += 1
            else:
                s_n.insert(0, 1)
            i -= 1
    for i, s in enumerate(s_n):
        if s == -2:
            s_n[i] = '='
        elif s == -1:
            s_n[i] = '-'
        else:  # s in [0, 1, 2]
            s_n[i] = str(s)
    return ''.join(s_n)


with open('scratch.txt') as f:
    s_nums = f.read().split('\n')
    print(decimal_2_snafu(sum(snafu_2_decimal(s) for s in s_nums)))  # Part 1

