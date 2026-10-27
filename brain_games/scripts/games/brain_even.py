import random

import prompt

from brain_games.scripts.engine import run


def is_even_string(num: int) -> str:
    return "yes" if num % 2 == 0 else "no"


def number_in_range() -> int:
    return random.randrange(0, 100)


def get_target_value():
    number: int = number_in_range()
    target_value = is_even_string(number)

    print(f"Question: {number}")
    return target_value


def main():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    run(question, get_target_value, lambda: prompt.string("Your answer: "))
