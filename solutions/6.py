def solution(num_chars):
    with open("../data/6.txt") as f:
        line = next(iter(f))
        for i in range(len(line) - num_chars):
            if len(set(line[i:i + num_chars])) == num_chars:
                return i + num_chars


print(solution(4))
print(solution(14))
