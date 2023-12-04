import re
from collections import defaultdict

from aoc.utils.timing import timeit


@timeit
def part1(data):
    total = 0
    for line in data:
        if v := parse_card(line):
            total += 0 if len(v) == 0 else pow(2, len(v) - 1)
    return total


@timeit
def part2(data):
    copies = defaultdict(int)
    for i, line in enumerate(data):
        copies[i] += 1
        for x in range(i + 1, i + 1 + len(parse_card(line))):
            copies[x] += copies[i]
    return sum(copies.values())


def parse_card(card_text):
    pattern = r"Card\s+\d+: (.*) \| (.*)"
    match = re.match(pattern, card_text)
    if match:
        winning = re.findall(r"\d+", match.group(1))
        yours = re.findall(r"\d+", match.group(2))
        return set([int(v) for v in winning]).intersection([int(v) for v in yours])
    else:
        return None


if __name__ == "__main__":
    with open("aoc/day04/input_day04.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
