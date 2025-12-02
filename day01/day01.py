from dataclasses import dataclass
from typing import Literal, TypeGuard


def read_file(fp: str) -> str:
    with open(fp, "r") as file:
        return file.read()


content = read_file("day01/input1.txt")
lines = content.splitlines()

type RotationDirection = Literal["L", "R"]
type Rotation = tuple[RotationDirection, int]


def is_rotation_direction(s: str) -> TypeGuard[RotationDirection]:
    if s in {"L", "R"}:
        return True
    return False


def parse(lines: list[str]) -> list[Rotation]:
    rotations: list[Rotation] = []
    for line in lines:
        direction = line[0]
        if not is_rotation_direction(direction):
            raise ValueError(f"invalid rotation direction: {direction}")
        by = int(line[1:])
        rotations.append((direction, by))
    return rotations


rotations = parse(lines)


@dataclass
class Dial:
    value: int = 50
    size: int = 100

    zero_state_counter: int = 0
    zero_cross_counter: int = 0

    def rotate(self, direction: RotationDirection, by: int) -> None:
        print(f"{direction} {by}")
        value = self.value
        print(f"{value=}")
        if direction == "R":
            value += by
        elif direction == "L":
            value -= by

        corrected_value = value % self.size
        print(f"{corrected_value=}")
        full_rotations = abs(value // self.size)
        print(f"{full_rotations=}")

        self.value = corrected_value

        self.zero_cross_counter += full_rotations
        if self.value == 0:
            self.zero_state_counter += 1

        print("---")


dial = Dial(50)

for direction, by in rotations:
    dial.rotate(direction, by)

print(f"Part 1: {dial.zero_state_counter}")
print(f"Part 2: {dial.zero_cross_counter}")
