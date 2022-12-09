def move_head(head_x, head_y, direction):
    match direction:
        case 'R':
            return head_x + 1, head_y
        case 'L':
            return head_x - 1, head_y
        case 'U':
            return head_x, head_y + 1
        case 'D':
            return head_x, head_y - 1


def take_step(head_x, head_y, tail_x, tail_y):
    def is_close(a, b):
        return abs(a - b) <= 1

    def helper(head_loc, tail_loc):
        if is_close(tail_loc, head_loc):
            return head_loc
        return head_loc - 1 if tail_loc < head_loc else head_loc + 1

    if is_close(head_x, tail_x) and is_close(head_y, tail_y):
        return tail_x, tail_y
    return helper(head_x, tail_x), helper(head_y, tail_y)


def solution(rope_length):
    with open("../data/9.txt") as f:
        rope = [(0, 0)] * rope_length
        tail_locations = {(0, 0)}
        for line in f:
            direction, steps = line[0], int(line[2:])
            for i in range(steps):
                rope[-1] = move_head(*rope[-1], direction)
                for j in reversed(range(rope_length - 1)):
                    rope[j] = take_step(*rope[j + 1], *rope[j])
                tail_locations.add(rope[0])
        return len(tail_locations)


print(solution(2))  # Part 1
print(solution(10))  # Part 2
