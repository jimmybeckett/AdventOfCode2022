import re
import utils


def solution(reverse):
    with utils.get_input(2022, 5) as f:
        stacks = []
        for line in f:
            if line[1] == "1":
                break
            for i in range(len(line) // 4):
                if i == len(stacks):
                    stacks.append([])
                if (c := line[i * 4 + 1]) != " ":
                    stacks[i].insert(0, c)
        move_re = re.compile(r"move (\d+) from (\d+) to (\d+)")
        for line in f:
            if match := move_re.match(line):
                n, src, dest = map(int, match.groups())
                crates = stacks[src - 1][-n:]
                if reverse:
                    crates = reversed(crates)
                stacks[dest - 1] += crates
                del stacks[src - 1][-n:]
        return ''.join(stack[-1] for stack in stacks)


print(solution(reverse=True))
print(solution(reverse=False))
