from pascal_intepreter.part3.custom_interpreter import Interpreter


def test_division_multiplication():
    interpreter = Interpreter('7 - 3 + 2 - 1')
    result = interpreter.expr()
    expected_result = 5
    assert result == expected_result
