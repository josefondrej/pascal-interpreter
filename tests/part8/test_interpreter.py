import pytest

from pascal_intepreter.part8.interpreter import Interpreter
from pascal_intepreter.part8.lexer import Lexer
from pascal_intepreter.part8.parser import Parser


@pytest.mark.parametrize('text, expected_result', [
    ('2 + 4 - 5 * (6 + 7) + - - - 9 * 3 - 2 * (((4-3)) * 2)', -90),
    ('- 3', -3),
    ('+ 3', 3),
    ('5 - - - + - 3', 8),
    ('5 - - - + - (3 + 4) - +2', 10)
])
def test_interpret(text, expected_result):
    text = '2 + 4 - 5 * (6 + 7) + - - - 9 * 3 - 2 * (((4-3)) * 2)'
    interpreter = Interpreter(Parser(Lexer(text)))
    assert interpreter.interpret() == -90
