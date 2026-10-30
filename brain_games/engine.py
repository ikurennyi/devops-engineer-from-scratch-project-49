import random
from typing import cast

import prompt

ROUNDS_TO_WIN = 3


def greeting(description: str | None = None) -> str:
    print("Welcome to the Brain Games!")
    user_name = cast(str, prompt.string("May I have your name? "))
    print(f"Hello, {user_name}!")

    if description is not None:
        print(description)
    return user_name


def number_in_range(start: int = 0, end: int = 100) -> int:
    return random.randrange(start, end)


def run(game) -> None:
    user_name = greeting(game.DESCRIPTION)
    correct_answers = 0

    while correct_answers != ROUNDS_TO_WIN:
        task, correct_answer = game.generate_round()
        print(f"Question: {task}")
        answer = cast(str, prompt.string("Your answer: "))

        if answer == correct_answer:
            correct_answers += 1
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
