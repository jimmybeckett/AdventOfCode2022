import utils

elves = [0]

with utils.get_input(2022, 1) as f:
    for line in f:
        if line == '\n':
            elves.append(0)
        else:
            elves[-1] += int(line)

elves.sort(reverse=True)

print(elves[0])
print(sum(elves[:3]))
