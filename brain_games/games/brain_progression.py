import random

from brain_games.engine import number_in_range, read_answer_as_int

DESCRIPTION = "What number is missing in the progression?"

PROGRESSION_MIN_LENGTH = 5
PROGRESSION_MAX_LENGTH = 10

read_answer = read_answer_as_int


def generate_progression(start: int, step: int, length: int) -> list[int]:
    return [start + index * step for index in range(length)]


def format_progression(progression: list[int], hidden_index: int) -> str:
    parts = [
        ".." if index == hidden_index else str(value)
        for index, value in enumerate(progression)
    ]
    return " ".join(parts)


def generate_round() -> tuple[str, int]:
    length = random.randrange(
        PROGRESSION_MIN_LENGTH,
        PROGRESSION_MAX_LENGTH + 1,
    )
    start = number_in_range()
    step = number_in_range(1, 10)
    progression = generate_progression(start, step, length)
    hidden_index = random.randrange(length)
    correct_answer = progression[hidden_index]
    task = format_progression(progression, hidden_index)
    return task, correct_answer
