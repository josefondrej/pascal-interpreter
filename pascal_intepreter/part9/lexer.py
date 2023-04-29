from pascal_intepreter.part9.token import Token
from pascal_intepreter.part9.token_type import SEMI, INTEGER, ID, ASSIGN, DOT, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, \
    EOF

RESERVED_KEYWORDS = {
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'END': Token('END', 'END')
}


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0

    def advance(self):
        self.pos += 1

    @property
    def current_char(self):
        if self.pos >= len(self.text):
            return None
        return self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def peek(self):
        pos = self.pos + 1
        if pos >= len(self.text):
            return None
        return self.text[pos]

    def _id(self) -> Token:
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        token = RESERVED_KEYWORDS.get(result.upper(), Token(ID, result))
        return token

    def _number(self) -> Token:
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(INTEGER, int(result))

    def get_next_token(self) -> Token:
        while self.current_char is not None:
            if self.current_char.isalpha():
                return self._id()

            if self.current_char == ':' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(ASSIGN, ':=')

            if self.current_char == ';':
                self.advance()
                return Token(SEMI, ';')

            if self.current_char == '.':
                self.advance()
                return Token(DOT, '.')

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self._number()

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            raise Exception(f'Invalid character: {self.current_char}')

        return Token(EOF, None)
