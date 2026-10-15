import pytest
from src.toolkit.converter import convert
from src.toolkit.errors import *

def test_length():
    assert convert(1000, "mm", "m") == pytest.approx(1.0)


def test_mass():
    assert convert(1.5, "kg", "g") == pytest.approx(1500.0)

def test_fahrenheit_to_celsius():
    assert convert(32, "f", "c") == pytest.approx(0.0)


def test_kelvin_to_fahrenheit():
    assert convert(273.15, "k", "f") == pytest.approx(32.0)


def test_kelvin_to_kelvin():
    assert convert(300, "k", "k") == pytest.approx(300.0)


def test_unknown_source_unit():
    with pytest.raises(Unknown_Unit_Error):
        convert(1, "abc", "m")


def test_fahrenheit_below_absolute_zero():
    with pytest.raises(Invalid_Temperature_Error):
        convert(-460, "f", "k")


def test_kelvin_below_absolute_zero():
    with pytest.raises(Invalid_Temperature_Error):
        convert(-1, "k", "c")

def test_temperature():
    assert convert(0, "c", "f") == pytest.approx(32.0)


def test_absolute_zero():
    assert convert(-273.15, "c", "k") == pytest.approx(0.0)


def test_uppercase_units():
    assert convert(1000, "MM", "M") == pytest.approx(1.0)


def test_incompatible_units():
    with pytest.raises(Incompatible_Units_Error):
        convert(1, "kg", "m")


def test_unknown_unit():
    with pytest.raises(Unknown_Unit_Error):
        convert(1, "m", "abc")


def test_below_absolute_zero():
    with pytest.raises(Invalid_Temperature_Error):
        convert(-274, "c", "k")