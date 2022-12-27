import re
from collections import deque


def get_cubes():
    with open('scratch2.txt') as f:
        return {tuple(int(n) for n in re.findall('\d+', line)) for line in f}


def adjacent(x, y, z):
    return {(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)}


def part_1():
    cubes = get_cubes()
    return sum(1 for cube in cubes for x in adjacent(*cube) if x not in cubes)


def part_2():
    cubes = get_cubes()
    m = max(c for cube in cubes for c in cube) + 1
    visited = {(m, m, m)}
    q = deque(visited)
    surface_area = 0
    while q:
        for _ in range(len(q)):
            cube = q.popleft()
            surface_area += sum(1 for adj in adjacent(*cube) if adj in cubes)
            for adj in adjacent(*cube):
                if adj not in cubes and adj not in visited and all(c in range(-1, m + 1) for c in adj):
                    q.append(adj)
                    visited.add(adj)
    return surface_area


print(part_1())
print(part_2())
