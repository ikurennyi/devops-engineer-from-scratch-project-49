import random
from typing import cast

import prompt

ROUNDS_TO_WIN = 3


def greeting(question: str | None = None) -> str:
    print("Welcome to the Brain Games!")
    user_name = cast(str, prompt.string("May I have your name? "))
    print(f"Hello, {user_name}!")

    if question is not None:
        print(question)
    return user_name


def number_in_range(start=0, end=100) -> int:
    return random.randrange(start, end)


def read_answer_as_int():
    user_input = input("Your answer: ")
    try:
        return int(user_input)
    except ValueError:
        return user_input


def run(question: str, get_target_value, read_answer) -> None:
    user_name = greeting(question)
    correct_answers = 0

    while correct_answers != ROUNDS_TO_WIN:
        target_value = get_target_value()
        answer = read_answer()

        if target_value == answer:
            correct_answers += 1
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong ansewer ;(. "
                f"Correct answer was '{target_value}'"
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
