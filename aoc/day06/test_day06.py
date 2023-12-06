from aoc.day06.day06 import part1, part2

data = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


def test_part1():
    assert part1(data) == 288


def test_part2():
    assert part2(71530, 940200) == 71503
