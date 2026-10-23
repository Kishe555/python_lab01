import sys

import pytest

from src.toolkit.__main__ import main


def test_cli_calc(monkeypatch, capsys):
    monkeypatch.setattr(
        sys, "argv", ["toolkit", "calc", "2+3*4"])

    main()

    result = capsys.readouterr()
    assert float(result.out) == 14
    assert result.err == ""


def test_cli_error(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["toolkit", "calc", "2+a"])

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2

    result = capsys.readouterr()
    assert result.out == ""
    assert result.err.strip() != ""