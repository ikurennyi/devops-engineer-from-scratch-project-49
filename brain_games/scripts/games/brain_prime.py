import prompt

from brain_games.scripts.engine import number_in_range, run


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


def get_target_value():
    number = number_in_range()
    target_value = is_prime_string(number)

    print(f"Question: {number}")
    return target_value


def main():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run(question, get_target_value, lambda: prompt.string("Your answer: "))
