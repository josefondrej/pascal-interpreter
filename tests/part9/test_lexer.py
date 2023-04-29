from pascal_intepreter.part9.lexer import Lexer


def test_get_next_token():
    lexer = Lexer('BEGIN a := 2; END.')
    assert str(lexer.get_next_token()) == "Token(ID, 'BEGIN')"
    assert str(lexer.get_next_token()) == "Token(ID, 'a')"
    assert str(lexer.get_next_token()) == "Token(ASSIGN, ':=')"
    assert str(lexer.get_next_token()) == "Token(INTEGER, 2)"
    assert str(lexer.get_next_token()) == "Token(SEMI, ';')"
    assert str(lexer.get_next_token()) == "Token(ID, 'END')"
    assert str(lexer.get_next_token()) == "Token(DOT, '.')"
    assert str(lexer.get_next_token()) == "Token(EOF, None)"
