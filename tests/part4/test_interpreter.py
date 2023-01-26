import pytest

from pascal_intepreter.part4.exercise_interpreter import Interpreter
from pascal_intepreter.part4.interpreter import Lexer


@pytest.mark.parametrize("text, expected_result", [
    ("7", 7),
    ("3 * 5", 15),
    ("3 / 2", 1.5),
    ("2 + 7 * 4", 30),
    ("7 - 8 / 4", 5),
    ("14 + 2 * 3 - 6 / 2", 17)
])
def test_expr(text, expected_result):
    lexer = Lexer(text)
    interpreter = Interpreter(lexer)
    result = interpreter.expr()
    assert result == expected_result
