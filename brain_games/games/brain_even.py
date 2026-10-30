from brain_games.engine import number_in_range

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_string(num: int) -> str:
    return "yes" if num % 2 == 0 else "no"


def generate_round() -> tuple[str, str]:
    number = number_in_range()
    correct_answer = is_even_string(number)
    return str(number), correct_answer
