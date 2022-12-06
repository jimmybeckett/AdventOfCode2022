def solution(num_chars):
    with open("../data/6.txt") as f:
        line = next(iter(f))
        for i in range(num_chars, len(line)):
            if len(set(line[i - num_chars:i])) == num_chars:
                return i


print(solution(4))
print(solution(14))
