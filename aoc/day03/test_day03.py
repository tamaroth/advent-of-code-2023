from aoc.day03 import day03


data = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def test_part1():
    assert day03.part1(data) == 4361


def test_part2():
    assert day03.part2(data) == 467835
