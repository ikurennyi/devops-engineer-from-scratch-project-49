import operator as op
import random

from brain_games.scripts.engine import run

MATH_OPERATORS = ["+", "-", "*"]
OPERATIONS = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
}


def number_in_range(end=10) -> int:
    return random.randrange(0, end)


def get_target_value():
    first_number = number_in_range()
    second_number = number_in_range(first_number or 10)
    op_symbol = random.choice(MATH_OPERATORS)

    target_value = OPERATIONS[op_symbol](first_number, second_number)

    print(f"Question: {first_number} {op_symbol} {second_number}")

    return target_value


def read_answer():
    user_input = input("Your answer: ")
    try:
        return int(user_input)
    except ValueError:
        return user_input


def main():
    question = "What is the result of the expression?"
    run(question, get_target_value, read_answer)
