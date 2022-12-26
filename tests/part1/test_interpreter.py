from pascal_intepreter.part1.interpreter import Interpreter


def test_expr():
    text = '3+5'
    interpreter = Interpreter(text)
    result = interpreter.expr()
    expected_result = 8
    assert result == expected_result
