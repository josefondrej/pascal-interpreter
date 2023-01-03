import math

from pascal_intepreter.part2.interpreter import Interpreter


def test_multiplication():
    # Exercise 1
    interpreter = Interpreter('5 * 7')
    result = interpreter.expr()
    expected_result = 35
    assert result == expected_result


def test_division():
    # Exercise 2
    interpreter = Interpreter('10 / 3')
    result = interpreter.expr()
    expected_result = 10 / 3
    assert math.isclose(result, expected_result)


def test_arbitrary_number_of_operations():
    # Exercise 3
    interpreter = Interpreter('9 - 5 + 3 + 11')
    result = interpreter.expr()
    expected_result = 18
    assert result == expected_result
