import brain_games.engine as engine
import brain_games.games.brain_progression as brain_progression
from brain_games.games.brain_progression import (
    format_progression,
    generate_progression,
    generate_round,
)
from brain_games.scripts.brain_progression import main


def test_generate_progression():
    assert generate_progression(5, 2, 5) == [5, 7, 9, 11, 13]


def test_format_progression():
    progression = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    assert format_progression(progression, 5) == "5 7 9 11 13 .. 17 19 21 23"


def test_generate_round(monkeypatch):
    def fake_randrange(start, stop=None):
        if stop is not None:
            return 10
        return 5

    def fake_number_in_range(start=0, end=100):
        return 5 if end == 100 else 2

    monkeypatch.setattr(
        brain_progression.random,
        "randrange",
        fake_randrange,
    )
    monkeypatch.setattr(
        brain_progression,
        "number_in_range",
        fake_number_in_range,
    )

    task, correct_answer = generate_round()
    assert correct_answer == "15"
    assert task == "5 7 9 11 13 .. 17 19 21 23"


def test_main_three_correct_answers(monkeypatch, capsys):
    answers = iter(["John", "15", "15", "15"])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(
        brain_progression,
        "generate_round",
        lambda: ("5 7 .. 9", "15"),
    )

    main()
    out = capsys.readouterr().out
    assert "Hello, John" in out
    assert "Congratulations, John" in out


def test_main_wrong_answer_exits_early(monkeypatch, capsys):
    answers = iter(["Dan", "1"])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(
        brain_progression,
        "generate_round",
        lambda: ("5 7 .. 9", "15"),
    )

    main()
    out = capsys.readouterr().out
    assert "wrong answer" in out
    assert "Let's try again, Dan!" in out
    assert "Congratulations" not in out


def test_main_non_integer_answer_exits_early(monkeypatch, capsys):
    answers = iter(["Dan", "not-a-number"])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(
        brain_progression,
        "generate_round",
        lambda: ("5 7 .. 9", "15"),
    )

    main()
    out = capsys.readouterr().out
    assert "'not-a-number' is wrong answer" in out
    assert "Let's try again, Dan!" in out
