from pascal_intepreter.part1.interpreter import Interpreter
from pascal_intepreter.part10.lexer import Lexer
from pascal_intepreter.part10.load_program import load_program
from pascal_intepreter.part10.parser import Parser


def test_interpret():
    program = load_program('program.pas')
    lexer = Lexer(program)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    interpreter.interpret()

    assert interpreter.GLOBAL_SCOPE['a'] == 2
    assert interpreter.GLOBAL_SCOPE['b'] == 25
    assert interpreter.GLOBAL_SCOPE['c'] == 27
    assert interpreter.GLOBAL_SCOPE['number'] == 2
    assert interpreter.GLOBAL_SCOPE['x'] == 11
    assert abs(interpreter.GLOBAL_SCOPE['y'] - 5.99714285714) < 1e-6
