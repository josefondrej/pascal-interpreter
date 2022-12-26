from pascal_intepreter.part1.token import Token
from pascal_intepreter.part1.token_types import TokenType


class Interpreter:
    def __init__(self, text: str):
        # client string input, e.g. "3+5"
        self.text: str = text
        # self.pos is an index into self.text
        self.pos: int = 0
        # current token instance
        self.current_token: Token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(TokenType.EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if current_char.isdigit():
            digit = ''
            while current_char.isdigit():
                digit += current_char
                self.pos += 1
                if self.pos > len(text) - 1:
                    break
                current_char = text[self.pos]

            token = Token(TokenType.INTEGER, int(digit))
            return token

        if current_char == '+':
            token = Token(TokenType.PLUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type: TokenType):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the current token to be a single-digit integer
        left = self.current_token
        self.eat(TokenType.INTEGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        self.eat(TokenType.PLUS)

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.eat(TokenType.INTEGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        result = left.value + right.value
        return result
