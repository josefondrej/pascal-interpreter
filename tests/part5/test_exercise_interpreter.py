import pytest

from pascal_intepreter.part5.exercise_interpreter import Lexer, Interpreter


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


def test_braced_expr():
    lexer = Lexer("7 + 3 * (10 / (12 / (3 + 1) - 1))")
    interpreter = Interpreter(lexer)
    result = interpreter.expr()
    assert result == 22
