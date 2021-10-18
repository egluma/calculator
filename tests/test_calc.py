import pytest
from project import Calculator

number_1 = 2.0
number_2 = 9.0
number_3 = -4.0
test_cases = [number_2, number_1, number_3]


@pytest.fixture
def calculator():
    return Calculator()


def verify_answer(expected, answer, memory):
    assert expected == answer
    assert expected == memory


def test_last_answer_init(calculator):
    assert calculator.memory == 0.0


def test_add(calculator):
    answer = calculator.add(number_1)
    verify_answer(2.0, answer, calculator.memory)


def test_subtract(calculator):
    answer = calculator.subtract(number_1)
    verify_answer(-2.0, answer, calculator.memory)


def test_multiply(calculator):
    calculator.memory = 3.0
    answer = calculator.multiply(number_2)
    verify_answer(27.0, answer, calculator.memory)


def test_divide(calculator):
    calculator.memory = 16.0
    answer = calculator.divide(number_1)
    verify_answer(8.0, answer, calculator.memory)


def test_divide_by_zero(calculator):
    calculator.memory = number_1
    answer = calculator.divide(0)
    assert 'Cannot divide by 0' in answer
    assert calculator.memory == number_1


def test_root(calculator):
    calculator.memory = 64.0
    answer = calculator.nthroot(number_1)
    verify_answer(8.0, answer, calculator.memory)


def test_multiple_additions(calculator):
    for case in test_cases:
        answer = calculator.add(case)
    verify_answer(7.0, answer, calculator.memory)


def test_multiple_subtractions(calculator):
    for case in test_cases:
        answer = calculator.subtract(case)
    verify_answer(-7.0, answer, calculator.memory)


def test_multiple_multiplications(calculator):
    calculator.memory = 0.1
    for case in test_cases:
        answer = calculator.multiply(case)
    verify_answer(-7.2, answer, calculator.memory)


def test_multiple_divisions(calculator):
    calculator.memory = 81
    for case in test_cases:
        answer = calculator.divide(case)
    verify_answer(-1.125, answer, calculator.memory)


def test_reset_memory(calculator):
    calculator.memory = 1.0
    for case in test_cases:
        calculator.divide(case)
    calculator.reset()
    assert calculator.memory == 0.0
