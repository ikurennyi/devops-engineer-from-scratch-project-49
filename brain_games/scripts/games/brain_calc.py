import operator as op
import random

from brain_games.scripts.engine import number_in_range, read_answer_as_int, run

MATH_OPERATORS = ["+", "-", "*"]
OPERATIONS = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
}


def get_target_value():
    first_number = number_in_range()
    second_number = number_in_range(0, 10)
    op_symbol = random.choice(MATH_OPERATORS)

    target_value = OPERATIONS[op_symbol](first_number, second_number)

    print(f"Question: {first_number} {op_symbol} {second_number}")

    return target_value


def main():
    question = "What is the result of the expression?"
    run(question, get_target_value, read_answer_as_int)
