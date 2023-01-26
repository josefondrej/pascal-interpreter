import pytest

from pascal_intepreter.part5.exercise_interpreter import Lexer, Interpreter


@pytest.mark.parametrize(
    "expression, expected_result",
    [("3", 3),
     ("2 + 7 * 4", 30),
     ("7 - 8 / 4", 5),
     ("14 + 2 * 3 - 6 / 2", 17),
     ("7 + 3 * (10 / (12 / (3 + 1) - 1))", 22),
     ("7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)", 10),
     ("7 + (((3 + 2)))", 12)])
def test_interpreter(expression, expected_result):
    lexer = Lexer(expression)
    interpreter = Interpreter(lexer)
    result = interpreter.expr()
    assert result == expected_result
