import re
from functools import reduce

from aoc.utils.timing import timeit


@timeit
def part1(data):
    parsed = parse_races(data)
    results = []
    for t, d in parsed:
        results.append(len(calculate_max_distances(t, d)))
    return reduce(lambda x, y: x * y, results)


@timeit
def part2(t, d):
    return len(calculate_max_distances(t, d))


def parse_races(data):
    times = re.findall(r"(\d+)", data[0])
    distances = re.findall(r"(\d+)", data[1])
    return list(zip([int(t) for t in times], [int(d) for d in distances]))


def calculate_max_distances(max_time, min_distance):
    distances = []
    for tth in range(max_time):
        ttd = max_time - tth
        distance = ttd * tth
        if distance > min_distance:
            distances.append(distance)
    return distances


if __name__ == "__main__":
    with open("aoc/day06/input_day06.txt") as f:
        data = f.read().splitlines()
    part1(data)
    t = 38677673
    d = 234102711571236
    part2(t, d)
