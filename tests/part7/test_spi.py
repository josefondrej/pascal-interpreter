import pytest

from pascal_intepreter.part7.spi import Lexer, Parser, Interpreter


@pytest.mark.parametrize(
    "text, expected_result",
    [("7 + 3 * (10 / (12 / (3 + 1) - 1))", 22),
     ("7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)", 10),
     ("7 + (((3 + 2)))", 12)])
def test_interpreter(text, expected_result):
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    assert result == expected_result
