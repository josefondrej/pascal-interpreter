from pascal_intepreter.part8.token import Token
from pascal_intepreter.part8.token_type import INTEGER, MUL, DIV, PLUS, MINUS, LPAREN, RPAREN


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.position = 0

    def get_next_token(self) -> Token:
        """
        load the next token (integer -- can have multiple characters, *, /, +, -, (, ), or end of file)
        skip any whitespace
        :return: the next token
        """
        while self.position < len(self.text):
            current_char = self.text[self.position]
            if current_char.isspace():
                self.position += 1
                continue
            if current_char.isdigit():
                return Token(INTEGER, self._get_integer())
            if current_char == '*':
                self.position += 1
                return Token(MUL, '*')
            if current_char == '/':
                self.position += 1
                return Token(DIV, '/')
            if current_char == '+':
                self.position += 1
                return Token(PLUS, '+')
            if current_char == '-':
                self.position += 1
                return Token(MINUS, '-')
            if current_char == '(':
                self.position += 1
                return Token(LPAREN, '(')
            if current_char == ')':
                self.position += 1
                return Token(RPAREN, ')')
            raise Exception(f'Invalid character: {current_char}')

        return Token('EOF', None)
    
    def _get_integer(self) -> int:
        """
        return a (multidigit) integer consumed from the input
        """
        result = ''
        while self.position < len(self.text) and self.text[self.position].isdigit():
            result += self.text[self.position]
            self.position += 1
        return int(result)
