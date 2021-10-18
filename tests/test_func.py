import pytest
import project as func

number_1 = 2.0
number_2 = 9.0
number_3 = -4.0


def test_addition():
    assert func.addition(number_1, number_2) == 11.0


def test_addition_negative_number():
    assert func.addition(number_2, number_3) == 5.0


def test_subtraction():
    assert func.subtraction(number_2, number_1) == 7.0


def test_subtraction_negative_result():
    assert func.subtraction(number_1, number_2) == -7.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        func.division(number_1, 0)
    assert "division by zero" in str(e.value)


def test_multiplication():
    assert func.multiplication(number_1, number_2) == 18.0


def test_division():
    assert func.division(number_2, number_1) == 4.5


def test_root():
    assert func.take_root(number_2, number_1) == 3.0

