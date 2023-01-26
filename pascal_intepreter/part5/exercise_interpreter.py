# Write an interpreter as described in this article off
# the top of your head, without peeking into the code from
# the article.
# Write some tests for your interpreter, and make sure they pass.
#
# Extend the interpreter to handle arithmetic expressions
# containing parentheses so that your interpreter could
# evaluate deeply nested arithmetic expressions like:
# 7 + 3 * (10 / (12 / (3 + 1) - 1))

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__()


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def get_next_token(self):
        pass  # TODO


class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def expr(self):
        pass  # TODO
