import pytest

from pascal_intepreter.part7.infix_to_lisp_translator import InfixToLISPTranslator


@pytest.mark.parametrize("text, expected_result", [
    ("2 + 3", "(+ 2 3)"),
    ("(2 + 3 * 5)", "(+ 2 (* 3 5))")])
def test_translate(text, expected_result):
    translator = InfixToLISPTranslator()
    result = translator.translate(text)
    print(result)
    print(expected_result)
    assert result == expected_result
