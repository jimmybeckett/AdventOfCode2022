import re

from tqdm import tqdm



def get_intervals(sensors, y):
    intervals = []  # [x_a, x_b]
    for (sensor_x, sensor_y), dist in sensors.items():
        y_diff = abs(y - sensor_y)
        if y_diff <= dist:
            intervals.append(sorted((sensor_x - dist + y_diff, sensor_x + dist - y_diff)))
    return sorted(intervals)


def not_possible_points(y, sensors):
    intervals = get_intervals(sensors, y)
    positions = 0
    x = intervals[0][0] - 1
    for int_start, int_end in intervals:
        if int_start > x:
            x = int_start
        if int_end >= x:
            positions += int_end - x
            x = int_end
    return positions


def possible_x(y, sensors, min_x, max_x):
    intervals = get_intervals(sensors, y)
    x = min_x
    for int_start, int_end in intervals:
        if x > max_x:
            break
        elif int_start > x:
            return x
        elif int_end > x:
            x = int_end


with open('scratch.txt') as f:
    sensors = {}
    for line in f:
        sensor_x, sensor_y, beacon_x, beacon_y = [int(n) for n in re.findall(r'-?\d+', line)]
        sensors[(sensor_x, sensor_y)] = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

    print(not_possible_points(2000000, sensors))  # part 1

    # part 2
    for y in tqdm(range(4000000)):
        if p := possible_x(y, sensors, 0, 4000000):
            print(p * 4000000 + y)
            break
