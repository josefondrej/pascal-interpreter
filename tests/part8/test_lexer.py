from pascal_intepreter.part8.lexer import Lexer
from pascal_intepreter.part8.token import Token
from pascal_intepreter.part8.token_type import INTEGER, PLUS, LPAREN, RPAREN, EOF, DIV, MINUS, MUL


def test_get_next_token():
    lexer = Lexer(' 21 +3 / 2 + (3 - 100) * 2')
    assert lexer.get_next_token() == Token(INTEGER, 21)
    assert lexer.get_next_token() == Token(PLUS, '+')
    assert lexer.get_next_token() == Token(INTEGER, 3)
    assert lexer.get_next_token() == Token(DIV, '/')
    assert lexer.get_next_token() == Token(INTEGER, 2)
    assert lexer.get_next_token() == Token(PLUS, '+')
    assert lexer.get_next_token() == Token(LPAREN, '(')
    assert lexer.get_next_token() == Token(INTEGER, 3)
    assert lexer.get_next_token() == Token(MINUS, '-')
    assert lexer.get_next_token() == Token(INTEGER, 100)
    assert lexer.get_next_token() == Token(RPAREN, ')')
    assert lexer.get_next_token() == Token(MUL, '*')
    assert lexer.get_next_token() == Token(INTEGER, 2)
    assert lexer.get_next_token() == Token(EOF, None)
    assert lexer.get_next_token() == Token(EOF, None)
