from aoc.utils.timing import timeit


def calculate(data: list[str]) -> int:
    result = 0
    for line in data:
        only_digits = "".join([c for c in line if c.isdigit()])
        result += int(only_digits[0]) * 10 + int(only_digits[-1])
    return result


@timeit
def part1(data: list[str]) -> int:
    return calculate(data)


@timeit
def part2(data: list[str]) -> int:
    new_data = []
    for line in data:
        new_data.append(replace_digit_word(line))
    return calculate(new_data)


def replace_digit_word(line: str) -> str:
    digit_words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]
    new_line = ""
    for i, char in enumerate(line):
        for word in digit_words:
            if line[i:].startswith(word):
                new_line += str(digit_words.index(word) + 1)
                break
        else:
            new_line += char
    return new_line


if __name__ == "__main__":
    with open("aoc/day01/input_day01.txt") as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
