import functools


def max_heights(lst):
    return functools.reduce(lambda res, n: res + [max(n, res[-1]) if res else n], lst, [])



def horizontal_visible(trees):
    visible = [[False] * len(trees[0]) for _ in trees]

    for r in range(len(trees)):
        l_heights, r_heights = [-1] + max_heights(trees[r])[:-1], list(reversed(max_heights(reversed(trees[r]))))[
                                                                  1:] + [-1]
        for c in range(len(trees[0])):
            if trees[r][c] > l_heights[c] or trees[r][c] > r_heights[c]:
                visible[r][c] = True
    return visible


def flip(trees):
    result = [[0] * len(trees[0]) for _ in range(len(trees))]
    for r in range(len(trees)):
        for c in range(len(trees[0])):
            result[(c + len(trees[0])) % len(trees[0])][(r + len(trees[0])) % len(trees[0])] = trees[r][c]
    return result


def part_1(trees):
    visible = horizontal_visible(trees)
    flipped_visible = horizontal_visible(flip(trees))
    return sum(
        sum(1 for c in range(len(trees[0])) if visible[r][c] or flipped_visible[c][r]) for r in range(len(trees)))

def scenic_score(trees, r, c):
    def view(move_fn):
        next_r, next_c = move_fn(r, c)
        trees_viewed = 0
        while 0 <= next_r < len(trees) and 0 <= next_c < len(trees[0]):
            trees_viewed += 1
            if trees[next_r][next_c] >= trees[r][c]:
                break
            next_r, next_c = move_fn(next_r, next_c)
        return trees_viewed

    l_view = view(lambda x, y: (x, y - 1))
    r_view = view(lambda x, y: (x, y + 1))
    up_view = view(lambda x, y: (x - 1, y))
    down_view = view(lambda x, y: (x + 1, y))
    return l_view * r_view * up_view * down_view


def part_2(trees):
    return max(scenic_score(trees, r, c) for r in range(len(trees)) for c in range(len(trees[0])))


with open("../data/8.txt") as f:
    trees = [[int(t) for t in line if t != '\n'] for line in f]
    print(part_1(trees))
    print(part_2(trees))
