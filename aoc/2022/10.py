import re
import utils


def get_signal():
    with utils.get_input(2022, 10) as f:
        x = 1
        signal = [x]
        instructions = []
        for line in f:
            instructions.append(0)
            if match := re.match(r"addx (-?\d+)", line):
                instructions.append(int(match.group(1)))
            x += instructions.pop(0)
            signal.append(x)
        while instructions:
            x += instructions.pop(0)
            signal.append(x)
    return signal


def render_crt(signal, width, height):
    screen = [['.' for _ in range(width)] for _ in range(height)]
    for tick, x in enumerate(signal):
        if abs(x - tick % width) <= 1:
            screen[(tick // width) % height][tick % width] = '#'
    return screen


signal = get_signal()
print(sum(signal[i - 1] * i for i in range(20, 260, 40)))  # Part 1
print('\n'.join(str(row) for row in render_crt(signal, 40, 6)))  # Part 2
