import sys

from tqdm import tqdm


def spread(elves, max_rounds):
    elves = elves.copy()
    directions = [-1 + 0j, 1 + 0j, 0 - 1j, 0 + 1j]
    adjacent = [r + c for r in [-1, 0, 1] for c in [-1j, 0, 1j] if r + c != 0]
    for elf_round in tqdm(range(1, sys.maxsize if max_rounds == -1 else max_rounds + 1), total=-1,
                          file=sys.stdout):
        proposals = {}
        for elf in elves:
            for dir in directions:
                test_dirs = [dir - 1, dir, dir + 1] if dir.real == 0 else [dir - 1j, dir, dir + 1j]
                if any(elf + a in elves for a in adjacent) and all(
                        elf + d not in elves for d in test_dirs):
                    proposals.setdefault(elf + dir, []).append(elf)
                    break
        modified = False
        for proposal, proposers in proposals.items():
            if len(proposers) == 1:
                elves.remove(proposers[0])
                elves.add(proposal)
                modified = True
        if not modified:
            return elves, elf_round
        directions.append(directions.pop(0))
    return elves, max_rounds


def part_1(elves):
    moved_elves, _ = spread(elves, 10)
    rows, cols = zip(*[(int(elf.real), int(elf.imag)) for elf in moved_elves])
    return (max(rows) + 1 - min(rows)) * (max(cols) + 1 - min(cols)) - len(moved_elves)


def part_2(elves):
    _, rounds = spread(elves, -1)
    return rounds


with open('scratch.txt') as f:
    elves = {complex(r, c) for r, line in enumerate(f) for c, item in enumerate(line) if
             item == '#'}
    print(part_1(elves))
    print(part_2(elves))
