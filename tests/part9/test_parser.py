from pascal_intepreter.part9.lexer import Lexer
from pascal_intepreter.part9.parser import Parser


def test_parse():
    program_text = """
    BEGIN
    BEGIN
        number := 2;
        a := number;
        b := 10 * a + 10 * number / 4;
        c := a - - b
    END;
    x := 11;
    END.
    """
    lexer = Lexer(program_text)
    parser = Parser(lexer)
    ast = parser.parse()
    expected_ast_str = \
        "Compound([" \
        "   Compound([" \
        "       Assign(" \
        "           Var(Token(ID, 'number')), " \
        "           Token(ASSIGN, ':='), " \
        "           Num(Token(INTEGER, 2))" \
        "       ), " \
        "       Assign(" \
        "           Var(Token(ID, 'a')), " \
        "           Token(ASSIGN, ':='), " \
        "           Var(Token(ID, 'number'))" \
        "       ), " \
        "       Assign(" \
        "           Var(Token(ID, 'b')), " \
        "           Token(ASSIGN, ':='), " \
        "           BinOp(" \
        "               BinOp(" \
        "                   Num(Token(INTEGER, 10)), " \
        "                   Token(MUL, '*'), " \
        "                   Var(Token(ID, 'a'))" \
        "               ), " \
        "               Token(PLUS, '+'), " \
        "               BinOp(" \
        "                   BinOp(" \
        "                       Num(Token(INTEGER, 10)), " \
        "                       Token(MUL, '*'), " \
        "                       Var(Token(ID, 'number'))" \
        "                   ), " \
        "                   Token(DIV, '/'), " \
        "                   Num(Token(INTEGER, 4))" \
        "                   )" \
        "               )" \
        "           ), " \
        "       Assign(" \
        "           Var(Token(ID, 'c')), " \
        "           Token(ASSIGN, ':='), " \
        "           BinOp(" \
        "               Var(Token(ID, 'a')), " \
        "               Token(MINUS, '-'), " \
        "               UnaryOp(Token(MINUS, '-'), " \
        "               Var(Token(ID, 'b'))" \
        "           )" \
        "       )" \
        "   )" \
        "   ]), " \
        "   Assign(Var(Token(ID, 'x')), Token(ASSIGN, ':='), Num(Token(INTEGER, 11))), " \
        "   NoOp()" \
        "])"

    assert str(ast).replace(' ', '') == expected_ast_str.replace(' ', '')
