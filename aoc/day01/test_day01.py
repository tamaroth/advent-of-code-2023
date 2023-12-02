from aoc.day01 import day01


def test_day01_part1():
    data = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    assert day01.part1(data) == 142


def test_day01_part2():
    data = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert day01.part2(data) == 281
