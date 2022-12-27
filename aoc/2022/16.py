import itertools
import re
from collections import deque

from tqdm import tqdm


def dist(start, end, connections):
    q = deque([start])
    visited = set(q)
    d = 0
    while q:
        for _ in range(len(q)):
            valve = q.popleft()
            if valve == end:
                return d
            for connected_valve in connections[valve]:
                if connected_valve not in visited:
                    visited.add(connected_valve)
                    q.append(connected_valve)
        d += 1
    return d


# assumes flow_rates[start] == 0
def sequences(start, minutes, flow_rates, dists):
    def helper(start, open_valves, minutes_left):
        for end in dists[start]:
            if end not in open_valves and dists[start][end] < minutes_left and flow_rates[end] > 0:
                open_valves.append(end)
                yield from helper(end, open_valves, minutes_left - dists[start][end] - 1)
                open_valves.pop()
        yield open_valves.copy()

    return helper(start, [], minutes)


def pressure(start, sequence, flow_rates, minutes, dists):
    prev = start
    total_pressure = 0
    for valve in sequence:
        minutes -= dists[prev][valve] + 1
        total_pressure += minutes * flow_rates[valve]
        prev = valve
    return total_pressure


with open('scratch.txt') as f:
    connections = {}
    flow_rates = {}
    for line in f:
        valves = re.findall(r'[A-Z][A-Z]', line)
        connections[valves[0]] = valves[1:]
        flow_rates[valves[0]] = int(re.search(r'\d+', line).group())

    dists = {}
    for start in connections:
        for end in connections:
            if start != end:
                dists.setdefault(start, {})[end] = dist(start, end, connections)

    # Part 1
    print(max(pressure('AA', seq, flow_rates, 30, dists) for seq in sequences('AA', 30, flow_rates, dists)))


    m = [(pressure('AA', seq, flow_rates, 26, dists), set(seq)) for seq in sequences('AA', 26, flow_rates, dists)]
    # 235128 sequences
    # n = 0
    # for :
    #     n += 1
    # print(n)
    m.sort(reverse=True)
    n = 0
    for p1, seq1 in tqdm(m):
        for p2, seq2 in m:
            if p1 + p2 < n:
                break
            if not seq1.intersection(seq2):
                n = max(n, p1 + p2)
                break
    print(n)  # Part 2

    # for my_seq in sequences('AA', 26, flow_rates, dists):
    #     for elephant_seq in sequences('AA', 30, flow_rates, dists):
