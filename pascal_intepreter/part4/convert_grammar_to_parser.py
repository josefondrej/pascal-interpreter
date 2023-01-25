"""
Convert the grammar described in wiki.md to working parser
How to do this:
- each rule R of the grammar becomes a method R()
- alternatives (a1 | a2 | ...) become if-elif-else statements
- ()* become while statements
- each reference T becomes a call to the method eat -- eat(T)
"""
from typing import Any

INTEGER, MUL, DIV, EOF = 'INTEGER', 'MUL', 'DIV', 'EOF'


class Token:
    def __init__(self, type: str, value: Any):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'


class Parser:
    """
    expr: factor((MUL | DIV) factor) *
    factor: INTEGER
    """

    def __init__(self, expression: str):
        self.expression = expression
        self.position = 0
        self.current_token = self._next_token()

    def _next_token(self):
        if self.position >= len(self.expression):
            return Token(EOF, None)

        while self.expression[self.position] == ' ':
            self.position += 1

        if self.expression[self.position] == '/':
            self.position += 1
            return Token(DIV, None)

        if self.expression[self.position] == '*':
            self.position += 1
            return Token(DIV, None)

        str_int = ''
        while self.position < len(self.expression) and self.expression[self.position].isdigit():
            str_int += self.expression[self.position]
            self.position += 1

        return Token(INTEGER, int(str_int))

    def eat(self, token_type):
        print(self.current_token)
        if self.current_token.type != token_type:
            raise Exception('Syntax error, expected: ' + token_type)

        self.current_token = self._next_token()

    def factor(self):
        self.eat(INTEGER)

    def expr(self):
        self.factor()

        while self.current_token.type in (MUL, DIV):
            if self.current_token.type == MUL:
                self.eat(MUL)
            elif self.current_token.type == DIV:
                self.eat(DIV)
            self.factor()


if __name__ == '__main__':
    Parser('3*6').expr()
