import brain_games.scripts.engine as engine
import brain_games.scripts.games.brain_calc as brain_calc
from brain_games.scripts.games.brain_calc import get_target_value, main


def test_get_target_value_addition(monkeypatch, capsys):
    def fake_range(start=0, end=100):
        return 4 if end == 100 else 5

    monkeypatch.setattr(brain_calc, "number_in_range", fake_range)
    monkeypatch.setattr(brain_calc.random, "choice", lambda _: "+")

    assert get_target_value() == 9
    out = capsys.readouterr().out
    assert "Question: 4 + 5" in out


def test_main_three_correct_answers(monkeypatch, capsys):
    names = iter(["John"])
    answers = iter([9, 9, 9])
    monkeypatch.setattr(
        engine.prompt,
        "string",
        lambda _prompt: next(names),
    )
    monkeypatch.setattr(
        brain_calc,
        "read_answer_as_int",
        lambda: next(answers),
    )
    monkeypatch.setattr(brain_calc, "get_target_value", lambda: 9)

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
    monkeypatch.setattr(brain_calc, "read_answer_as_int", lambda: 0)
    monkeypatch.setattr(brain_calc, "get_target_value", lambda: 5)

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
    monkeypatch.setattr(brain_calc, "read_answer_as_int", lambda: "not-a-number")
    monkeypatch.setattr(brain_calc, "get_target_value", lambda: 5)

    main()
    out = capsys.readouterr().out
    assert "'not-a-number' is wrong ansewer" in out
    assert "Let's try again, Dan!" in out
