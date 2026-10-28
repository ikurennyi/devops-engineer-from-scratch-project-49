import prompt

from brain_games.engine import number_in_range

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def is_prime_string(num: int) -> str:
    return "yes" if is_prime(num) else "no"


def generate_round() -> tuple[str, str]:
    number = number_in_range()
    correct_answer = is_prime_string(number)
    return str(number), correct_answer


def read_answer():
    return prompt.string("Your answer: ")
