from pascal_intepreter.part3.interpreter import Interpreter


def test_division_multiplication():
    interpreter = Interpreter('7 * 4 / 2 * 3')
    result = interpreter.expr()
    expected_result = 42
    assert result == expected_result
