import random

from brain_games.scripts.engine import number_in_range, read_answer_as_int, run

PROGRESSION_MIN_LENGTH = 5
PROGRESSION_MAX_LENGTH = 10


def generate_progression(start: int, step: int, length: int) -> list[int]:
    return [start + index * step for index in range(length)]


def format_progression(progression: list[int], hidden_index: int) -> str:
    parts = [
        ".." if index == hidden_index else str(value)
        for index, value in enumerate(progression)
    ]
    return " ".join(parts)


def get_target_value():
    length = random.randrange(
        PROGRESSION_MIN_LENGTH,
        PROGRESSION_MAX_LENGTH + 1,
    )
    start = number_in_range()
    step = number_in_range(1, 10)
    progression = generate_progression(start, step, length)
    hidden_index = random.randrange(length)
    target_value = progression[hidden_index]

    print(f"Question: {format_progression(progression, hidden_index)}")

    return target_value


def main():
    question = "What number is missing in the progression?"
    run(question, get_target_value, read_answer_as_int)
