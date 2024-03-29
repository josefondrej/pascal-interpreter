from pascal_intepreter.part9.interpreter import Interpreter
from pascal_intepreter.part9.lexer import Lexer
from pascal_intepreter.part9.parser import Parser


def test_interpret():
    program_text = """\
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
    interpreter = Interpreter(parser)
    interpreter.interpret()
    assert interpreter.GLOBAL_SCOPE == {'a': 2, 'x': 11, 'c': 27, 'b': 25, 'number': 2}


def test_interpret_exercise_1():
    program_text = """
    BEGIN

    BEGIN
        number := 2;
        a := NumBer;
        B := 10 * a + 10 * NUMBER / 4;
        c := a - - b
    end;

    x := 11;
    END.
    """
    lexer = Lexer(program_text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    interpreter.interpret()
    assert interpreter.GLOBAL_SCOPE == {'a': 2, 'x': 11, 'c': 27, 'b': 25, 'number': 2}


def test_interpret_exercise_2():
    program_text = """
    BEGIN
        a := 5 div 3 + 1;
        b := a * 10 div 2;
    END.
    """
    lexer = Lexer(program_text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    interpreter.interpret()
    assert interpreter.GLOBAL_SCOPE == {'a': 2, 'b': 10}


def test_interpret_exercise_3():
    program_text = """
    BEGIN
        _a := 5 div 3 + 1;
        b := _a * 10 div 2;
    END.
    """
    lexer = Lexer(program_text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    interpreter.interpret()
    assert interpreter.GLOBAL_SCOPE == {'_a': 2, 'b': 10}
