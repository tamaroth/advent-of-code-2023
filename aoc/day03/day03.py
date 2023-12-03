import re

from aoc.utils.timing import timeit


@timeit
def part1(data) -> int:
    total = 0
    symbol_map = get_symbol_map(data)
    for _, symbol in symbol_map.items():
        for gear in symbol.values():
            for number in gear:
                total += number
    return total


@timeit
def part2(data) -> int:
    symbol_map = get_symbol_map(data)
    return calculate_gear_ratios(symbol_map)


def get_symbol_map(data):
    symbol_map = read_symbols(data)
    for y, line in enumerate(data):
        for match in re.finditer(r"\d+", line):
            x_st = match.start()
            x_end = match.end()
            number = int(match.group())
            adjacent_symbols_positions = get_adjacent_symbols_positions(
                symbol_map, x_st, x_end, y
            )
            for symbol_position in adjacent_symbols_positions:
                for numbers in symbol_map[symbol_position].values():
                    numbers.append(number)
    return symbol_map


def read_symbols(data):
    symbol_map = {}
    for y, line in enumerate(data):
        for x, symbol in enumerate(line):
            if not symbol.isdigit() and symbol != ".":
                symbol_map[(x, y)] = {symbol: []}
    return symbol_map


def get_adjacent_symbols_positions(symbol_map, x_st, x_end, row):
    result = set()
    for y in range(row - 1, row + 2):
        for x in range(x_st - 1, x_end + 1):
            if (x, y) in symbol_map:
                result.add((x, y))
    return result


def calculate_gear_ratios(symbol_map):
    total_gear_ratios = 0
    for _, symbol in symbol_map.items():
        if gear := symbol.get("*"):
            if len(gear) == 2:
                total_gear_ratios += gear[0] * gear[1]
    return total_gear_ratios


if __name__ == "__main__":
    with open("aoc/day03/input_day03.txt", "r") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
