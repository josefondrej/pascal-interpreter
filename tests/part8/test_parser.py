from pascal_intepreter.part8.lexer import Lexer
from pascal_intepreter.part8.parser import Parser


def test_parse():
    lexer = Lexer(' 21 +3 / 2 + (3 - 100) * 2')
    parser = Parser(lexer)
    tree = parser.expr()
    assert str(tree) == '((21+(3/2))+((3-100)*2))'
