import random

import prompt


def number_in_range() -> int:
    return random.randrange(0, 100)


def is_even_string(num: int) -> str:
    return "yes" if num % 2 == 0 else "no"


def main():
    correct_answers = 0

    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}")

    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answers != 3:
        number: int = number_in_range()
        is_even = is_even_string(number)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if is_even == answer:
            correct_answers += 1
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong ansewer ;(. Correct answer was '{is_even}'"
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}")
