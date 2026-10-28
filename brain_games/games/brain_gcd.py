from brain_games.engine import number_in_range, read_answer_as_int

DESCRIPTION = "Find the greatest common divisor of given numbers."

read_answer = read_answer_as_int


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def generate_round() -> tuple[str, int]:
    first_number = number_in_range()
    second_number = number_in_range()
    correct_answer = gcd(first_number, second_number)
    task = f"{first_number} {second_number}"
    return task, correct_answer
