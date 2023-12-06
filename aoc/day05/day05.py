import re
from concurrent.futures import ThreadPoolExecutor

from aoc.utils.timing import timeit


@timeit
def part1(data):
    seeds, conversion_maps = parse_input(data)
    return find_closest_seed(seeds, conversion_maps)


@timeit
def part2(data):
    seeds, conversion_maps = parse_input(data)
    seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    last = None
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {
            executor.submit(run_for_seed_range, seed_range, conversion_maps)
            for seed_range in seed_ranges
        }
        for future in futures:
            result = future.result()
            if last is None or result < last:
                last = result
    return last


@timeit
def run_for_seed_range(seed_range, conversion_maps):
    return find_closest_seed(generate_seeds(seed_range), conversion_maps)


def generate_seeds(seed_range):
    print(f"ranging over {seed_range[0]} to {seed_range[0] + seed_range[1]}")
    initial_seed = seed_range[0]
    length = seed_range[1]
    for i in range(length):
        yield initial_seed + i


def parse_input(data):
    seeds = [int(v) for v in re.findall(r"\d+", data[0])]

    conversion_maps = {}
    source = None
    for line in data[2:]:
        map_type = re.findall(r"(\w+)-to-(\w+) map:", line)
        if map_type:
            source = map_type[0][0]
            dest = map_type[0][1]
            conversion_maps[source] = {
                "dest": dest,
                "ranges": [],
            }
            continue
        ranges = re.findall(r"(\d+) (\d+) (\d+)", line)
        if ranges:
            conversion_maps[source]["ranges"].append(
                (int(ranges[0][0]), int(ranges[0][1]), int(ranges[0][2]))
            )
    return seeds, conversion_maps


def find_closest_seed(seeds, conversion_maps):
    closest_distance = None
    source = "seed"
    for seed in seeds:
        mapping = conversion_maps[source]
        while True:
            ranges = mapping["ranges"]
            seed = calculate_new_seed(seed, ranges)
            dest = mapping["dest"]
            if dest == "location":
                break
            mapping = conversion_maps[dest]
        if closest_distance is None or seed < closest_distance:
            closest_distance = seed
    return closest_distance


def calculate_new_seed(seed, ranges):
    for target, start, range in ranges:
        if seed >= start and seed <= start + range:
            return seed - start + target
    return seed


if __name__ == "__main__":
    with open("aoc/day05/input_day05.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
