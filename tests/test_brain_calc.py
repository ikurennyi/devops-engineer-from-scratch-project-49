import brain_games.engine as engine
import brain_games.games.brain_calc as brain_calc
from brain_games.games.brain_calc import generate_round
from brain_games.scripts.brain_calc import main


def test_generate_round_addition(monkeypatch):
    def fake_range(start=0, end=100):
        return 4 if end == 100 else 5

    monkeypatch.setattr(brain_calc, "number_in_range", fake_range)
    monkeypatch.setattr(brain_calc.random, "choice", lambda _: "+")

    assert generate_round() == ("4 + 5", "9")


def test_main_three_correct_answers(monkeypatch, capsys):
    answers = iter(["John", "9", "9", "9"])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(brain_calc, "generate_round", lambda: ("4 + 5", "9"))

    main()
    out = capsys.readouterr().out
    assert "Hello, John" in out
    assert "Congratulations, John" in out


def test_main_wrong_answer_exits_early(monkeypatch, capsys):
    answers = iter(["Dan", "0"])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(brain_calc, "generate_round", lambda: ("1 + 1", "5"))

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
    monkeypatch.setattr(brain_calc, "generate_round", lambda: ("1 + 1", "5"))

    main()
    out = capsys.readouterr().out
    assert "'not-a-number' is wrong answer" in out
    assert "Let's try again, Dan!" in out
