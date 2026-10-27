from brain_games.scripts.engine import number_in_range, read_answer_as_int, run


#  alternative: from math import gcd
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def get_target_value():
    first_number = number_in_range()
    second_number = number_in_range()
    target_value = gcd(first_number, second_number)

    print(f"Question: {first_number} {second_number}")

    return target_value


def main():
    question = "Find the greatest common divisor of given numbers."
    run(question, get_target_value, read_answer_as_int)
