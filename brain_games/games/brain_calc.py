import operator as op
import random

from brain_games.engine import number_in_range

DESCRIPTION = "What is the result of the expression?"

MATH_OPERATORS = ["+", "-", "*"]
OPERATIONS = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
}


def generate_round() -> tuple[str, str]:
    first_number = number_in_range()
    second_number = number_in_range(0, 10)
    op_symbol = random.choice(MATH_OPERATORS)
    correct_answer = OPERATIONS[op_symbol](first_number, second_number)
    task = f"{first_number} {op_symbol} {second_number}"
    return task, str(correct_answer)
