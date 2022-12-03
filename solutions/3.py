def solution(fn):
    with open("../data/3.txt") as f:
        priority_sum = 0
        while line := f.readline().strip():
            item = fn(line, f).pop()
            priority_sum += ord(item) - (96 if item.islower() else 38)
        return priority_sum


print(solution(lambda line, _: set(line[:len(line)//2]) & set(line[len(line)//2:])))
print(solution(lambda line, f: set(line) & set(f.readline().strip()) & set(f.readline().strip())))
