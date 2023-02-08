import pytest

from pascal_intepreter.part7.infix_to_postfix_translator import InfixToPostfixTranslator


@pytest.mark.parametrize("text, expected_result", [
    ("(5 + 3) * 12 / 3", "5 3 + 12 * 3 /")])
def test_translate(text, expected_result):
    translator = InfixToPostfixTranslator()
    result = translator.translate(text)
    assert result == expected_result
