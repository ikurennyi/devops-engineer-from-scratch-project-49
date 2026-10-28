import brain_games.games.brain_prime as brain_prime
from brain_games.games.brain_prime import (
    is_prime,
    is_prime_string,
)
from brain_games.scripts.brain_prime import main


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(9) is False


def test_is_prime_string():
    assert is_prime_string(7) == "yes"
    assert is_prime_string(9) == "no"


def test_main_three_correct_answers(monkeypatch, capsys):
    answers = iter(["John", "yes", "yes", "yes"])
    monkeypatch.setattr(
        brain_prime.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(brain_prime, "number_in_range", lambda: 7)
    main()
    out = capsys.readouterr().out
    assert "Hello, John" in out
    assert "Congratulations, John" in out


def test_main_wrong_answer_exits_early(monkeypatch, capsys):
    answers = iter(["Dan", "yes"])
    monkeypatch.setattr(
        brain_prime.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(brain_prime, "number_in_range", lambda: 9)
    main()
    out = capsys.readouterr().out
    assert "wrong answer" in out
    assert "Let's try again, Dan!" in out
    assert "Congratulations" not in out
