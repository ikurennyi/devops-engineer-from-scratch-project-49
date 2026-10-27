import brain_games.scripts.engine as engine
import brain_games.scripts.games.brain_gcd as brain_gcd
from brain_games.scripts.games.brain_gcd import gcd, get_target_value, main


def test_gcd():
    assert gcd(12, 8) == 4
    assert gcd(0, 5) == 5
    assert gcd(17, 17) == 17


def test_get_target_value(monkeypatch, capsys):
    values = iter([12, 8])
    monkeypatch.setattr(brain_gcd, "number_in_range", lambda: next(values))

    assert get_target_value() == 4
    out = capsys.readouterr().out
    assert "Question: 12 8" in out


def test_main_three_correct_answers(monkeypatch, capsys):
    names = iter(["John"])
    answers = iter([4, 4, 4])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(names),
    )
    monkeypatch.setattr(
        brain_gcd,
        "read_answer_as_int",
        lambda: next(answers),
    )
    monkeypatch.setattr(brain_gcd, "get_target_value", lambda: 4)

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
    monkeypatch.setattr(brain_gcd, "read_answer_as_int", lambda: 0)
    monkeypatch.setattr(brain_gcd, "get_target_value", lambda: 5)

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
    monkeypatch.setattr(brain_gcd, "read_answer_as_int", lambda: "not-a-number")
    monkeypatch.setattr(brain_gcd, "get_target_value", lambda: 5)

    main()
    out = capsys.readouterr().out
    assert "'not-a-number' is wrong ansewer" in out
    assert "Let's try again, Dan!" in out
