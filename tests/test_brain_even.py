import brain_games.scripts.brain_even as brain_even
from brain_games.scripts.brain_even import is_even_string, main


def test_is_even_string():
    assert is_even_string(2) == "yes"
    assert is_even_string(7) == "no"


def test_main_three_correct_answers(monkeypatch, capsys):
    answers = iter(["John", "yes", "yes", "yes"])
    monkeypatch.setattr(
        brain_even.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(brain_even, "number_in_range", lambda: 2)
    main()
    out = capsys.readouterr().out
    assert "Hello, John" in out
    assert "Congratulations, John" in out


def test_main_wrong_answer_exits_early(monkeypatch, capsys):
    answers = iter(["Dan", "yes"])
    monkeypatch.setattr(
        brain_even.prompt,
        "string",
        lambda _prompt: next(answers),
    )
    monkeypatch.setattr(brain_even, "number_in_range", lambda: 7)
    main()
    out = capsys.readouterr().out
    assert "wrong ansewer" in out  # опечатка как в вашем print
    assert "Let's try again, Dan!" in out
    assert "Congratulations" not in out
