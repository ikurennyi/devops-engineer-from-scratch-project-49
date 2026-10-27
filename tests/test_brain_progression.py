import brain_games.scripts.engine as engine
import brain_games.scripts.games.brain_progression as brain_progression
from brain_games.scripts.games.brain_progression import (
    format_progression,
    generate_progression,
    get_target_value,
    main,
)


def test_generate_progression():
    assert generate_progression(5, 2, 5) == [5, 7, 9, 11, 13]


def test_format_progression():
    progression = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    assert format_progression(progression, 5) == "5 7 9 11 13 .. 17 19 21 23"


def test_get_target_value(monkeypatch, capsys):
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

    assert get_target_value() == 15
    out = capsys.readouterr().out
    assert "Question: 5 7 9 11 13 .. 17 19 21 23" in out


def test_main_three_correct_answers(monkeypatch, capsys):
    names = iter(["John"])
    answers = iter([15, 15, 15])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(names),
    )
    monkeypatch.setattr(
        brain_progression,
        "read_answer_as_int",
        lambda: next(answers),
    )
    monkeypatch.setattr(brain_progression, "get_target_value", lambda: 15)

    main()
    out = capsys.readouterr().out
    assert "Hello, John" in out
    assert "Congratulations, John" in out


def test_main_wrong_answer_exits_early(monkeypatch, capsys):
    names = iter(["Dan"])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(names),
    )
    monkeypatch.setattr(brain_progression, "read_answer_as_int", lambda: 1)
    monkeypatch.setattr(brain_progression, "get_target_value", lambda: 15)

    main()
    out = capsys.readouterr().out
    assert "wrong ansewer" in out
    assert "Let's try again, Dan!" in out
    assert "Congratulations" not in out


def test_main_non_integer_answer_exits_early(monkeypatch, capsys):
    names = iter(["Dan"])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(names),
    )
    monkeypatch.setattr(
        brain_progression,
        "read_answer_as_int",
        lambda: "not-a-number",
    )
    monkeypatch.setattr(brain_progression, "get_target_value", lambda: 15)

    main()
    out = capsys.readouterr().out
    assert "'not-a-number' is wrong ansewer" in out
    assert "Let's try again, Dan!" in out
