# Write an interpreter that handles arithmetic expressions like “7 - 3 + 2 - 1” from scratch.
# Use any programming language you’re comfortable with and write it off the top of your head without looking
# at the examples. When you do that, think about components involved: a lexer that takes an input and converts it into
# a stream of tokens, a parser that feeds off the stream of the tokens provided by the lexer and tries to recognize
# a structure in that stream, and an interpreter that generates results after the parser has successfully parsed
# (recognized) a valid arithmetic expression. String those pieces together. Spend some time translating the knowledge
# you’ve acquired into a working interpreter for arithmetic expressions.
from typing import Iterator, List


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Interpreter:
    def __init__(self, text: str):
        self.lexer = Lexer(text)

    def next_expected(self, token_types: List[str]) -> Token:
        token = next(self.lexer)
        if token.type in token_types:
            return token
        raise Exception('Invalid syntax')

    def expr(self) -> int:
        first_integer = self.next_expected(INTEGER)
        result = first_integer.value
        while True:
            operation = self.next_expected([PLUS, MINUS, EOF])
            if operation.type == EOF:
                break
            next_integer = self.next_expected([INTEGER])
            if operation.type == PLUS:
                result += next_integer.value
            elif operation.type == MINUS:
                result -= next_integer.value

        return result


class Lexer(Iterator):
    def __init__(self, expression: str):
        self._expression = expression
        self._current_char = self._expression[0]
        self._pos = 0

    def advance(self):
        self._pos += 1
        if self._pos > len(self._expression) - 1:
            self._current_char = None
        else:
            self._current_char = self._expression[self._pos]

    def _skip_whitespace(self) -> bool:
        if self._current_char is None:
            return

        while self._current_char.isspace():
            self.advance()

    def _integer(self) -> int:
        result = ''
        while self._current_char is not None and self._current_char.isdigit():
            result += self._current_char
            self.advance()
        return int(result)

    def __next__(self) -> Token:
        self._skip_whitespace()
        if self._current_char is None:
            return Token(EOF, None)
        if self._current_char.isdigit():
            return Token(INTEGER, self._integer())
        if self._current_char == '+':
            self.advance()
            return Token(PLUS, '+')
        if self._current_char == '-':
            self.advance()
            return Token(MINUS, '-')
        raise Exception('Invalid syntax')
