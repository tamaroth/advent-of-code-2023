from __future__ import annotations

import dataclasses
import re
from collections import defaultdict
from functools import reduce
from operator import mul

from aoc.utils.timing import timeit

MAX_VALUES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


@dataclasses.dataclass
class Game:
    id: int
    max_cubes: dict[str, int] = dataclasses.field(
        default_factory=lambda: defaultdict(int)
    )

    @classmethod
    def from_str(cls, line: str) -> "Game":
        if m := re.match(r"Game (?P<game_id>\d+): (?P<rounds>.+)", line):
            max_cubes: dict[str, int] = defaultdict(int)
            for round in m.group("rounds").split(sep="; "):
                for colour in round.split(sep=", "):
                    amount, name = colour.split(sep=" ")
                    max_cubes[name] = max(max_cubes[name], int(amount))
            return cls(int(m.group("game_id")), max_cubes)

        raise ValueError(f"Invalid game: {line}")

    def is_possible(self) -> bool:
        return all(
            [count <= MAX_VALUES[colour] for colour, count in self.max_cubes.items()]
        )

    def get_power(self) -> int:
        return reduce(mul, self.max_cubes.values())


@timeit
def part1(data: list[str]) -> int:
    result = 0
    for line in data:
        game = Game.from_str(line)
        result += game.id if game.is_possible() else 0
    return result


@timeit
def part2(data: list[str]) -> int:
    result = 0
    for line in data:
        game = Game.from_str(line)
        result += game.get_power()
    return result


if __name__ == "__main__":
    with open("aoc/day02/input_day02.txt") as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
