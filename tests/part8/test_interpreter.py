from pascal_intepreter.part8.interpreter import Interpreter
from pascal_intepreter.part8.lexer import Lexer
from pascal_intepreter.part8.parser import Parser


def test_interpret():
    text = '2 + 4 - 5 * (6 + 7) + - - - 9 * 3 - 2 * (((4-3)) * 2)'
    interpreter = Interpreter(Parser(Lexer(text)))
    assert interpreter.interpret() == -90
