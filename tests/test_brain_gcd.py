import brain_games.engine as engine
import brain_games.games.brain_gcd as brain_gcd
from brain_games.games.brain_gcd import gcd, generate_round
from brain_games.scripts.brain_gcd import main


def test_gcd():
    assert gcd(12, 8) == 4
    assert gcd(0, 5) == 5
    assert gcd(17, 17) == 17


def test_generate_round(monkeypatch):
    values = iter([12, 8])
    monkeypatch.setattr(brain_gcd, "number_in_range", lambda: next(values))

    assert generate_round() == ("12 8", "4")


def test_main_three_correct_answers(monkeypatch, capsys):
    answers = iter(["John", "4", "4", "4"])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(brain_gcd, "generate_round", lambda: ("12 8", "4"))

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
    monkeypatch.setattr(brain_gcd, "generate_round", lambda: ("1 1", "5"))

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
    monkeypatch.setattr(brain_gcd, "generate_round", lambda: ("1 1", "5"))

    main()
    out = capsys.readouterr().out
    assert "'not-a-number' is wrong answer" in out
    assert "Let's try again, Dan!" in out
