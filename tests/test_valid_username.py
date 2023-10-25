import pytest
from src.username import username


def test_valid_username(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "JohnDoe123")

    user = username()

    assert len(user) > 3
    assert len(user) < 20