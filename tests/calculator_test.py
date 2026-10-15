import pytest
from src.toolkit.calculator import *
from src.toolkit.errors import *

def test_priority():
    assert solve("2+3*4") == 14


def test_division():
    assert solve("10/4") == pytest.approx(2.5)


def test_negative_number():
    assert solve("2*-3") == -6


def test_decimal_numbers():
    assert solve("1.5+2.25") == pytest.approx(3.75)


def test_empty_expression():
    with pytest.raises(Invalid_Expression_Error):
        solve("")


def test_invalid_symbol():
    with pytest.raises(Invalid_Symbol_Error):
        solve("2+a")


def test_invalid_operators():
    with pytest.raises(Invalid_Expression_Error):
        solve("2*/3")

def test_subtraction():
    assert solve("10-3-2") == pytest.approx(5.0)


def test_division_then_addition():
    assert solve("10/4+1") == pytest.approx(3.5)


def test_spaces():
    assert solve(" 2 + 3 * 4 ") == pytest.approx(14.0)


def test_unary_plus():
    assert solve("+2*3") == pytest.approx(6.0)


def test_operator_at_start():
    with pytest.raises(Invalid_Expression_Error):
        solve("*2")


def test_missing_operator():
    with pytest.raises(Invalid_Expression_Error):
        solve("2 3")


def test_operator_at_end():
    with pytest.raises(Invalid_Expression_Error):
        solve("2*")

def test_division_by_zero():
    with pytest.raises(Division_By_Zero_Error):
        solve("1/0")
