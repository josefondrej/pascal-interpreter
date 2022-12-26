from pascal_intepreter.part1.interpreter import Interpreter


def test_expr():
    text = '3+5'
    interpreter = Interpreter(text)
    result = interpreter.expr()
    expected_result = 8
    assert result == expected_result


def test_expr_multicharacter_digits():
    text = '12+5'
    interpreter = Interpreter(text)
    result = interpreter.expr()
    expected_result = 17
    assert result == expected_result
