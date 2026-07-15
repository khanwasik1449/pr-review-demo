import pytest
from src.calculator import Calculator


def test_calculator_add():
    calc = Calculator()
    assert calc.add(2.0, 3.0) == 5.0
    assert calc.add(-1.0, 1.0) == 0.0


def test_calculator_subtract():
    calc = Calculator()
    assert calc.subtract(5.0, 3.0) == 2.0
    assert calc.subtract(0.0, 4.0) == -4.0


def test_calculator_multiply():
    calc = Calculator()
    assert calc.multiply(3.0, 4.0) == 12.0
    assert calc.multiply(-2.0, 3.0) == -6.0


def test_calculator_divide():
    calc = Calculator()
    assert calc.divide(6.0, 3.0) == 2.0
    assert calc.divide(5.0, 2.0) == 2.5


def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError) as excinfo:
        calc.divide(1.0, 0.0)
    assert "Cannot divide by zero" in str(excinfo.value)
