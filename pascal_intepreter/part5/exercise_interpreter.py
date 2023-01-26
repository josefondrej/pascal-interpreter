# Write an interpreter as described in this article off
# the top of your head, without peeking into the code from
# the article.
# Write some tests for your interpreter, and make sure they pass.
#
# Extend the interpreter to handle arithmetic expressions
# containing parentheses so that your interpreter could
# evaluate deeply nested arithmetic expressions like:
# 7 + 3 * (10 / (12 / (3 + 1) - 1))

INTEGER, DIV, MUL, PLUS, MINUS, EOF, LBRACE, RBRACE = \
    'INTEGER', 'DIV', 'MUL', 'PLUS', 'MINUS', 'EOF', '(', ')'


# expr: term ((PLUS | MINUS) term)*
# braced_expr: LBRACE expr RBRACE
# term: factor ((MUL | DIV) factor)*
# factor: INTEGER | braced_expr


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

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_integer_token(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(INTEGER, int(result))

    def get_next_token(self):
        if self.current_char is None:
            return Token(EOF, None)

        if self.current_char.isspace():
            self.skip_whitespace()

        if self.current_char.isdigit():
            return self.get_integer_token()

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
            return Token(LBRACE, '(')

        if self.current_char == ')':
            self.advance()
            return Token(RBRACE, ')')

        self.error()


class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == LBRACE:
            return self.braced_expr()
        elif token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        else:
            self.error()

    def term(self):
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result *= self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result /= self.factor()

        return result

    def braced_expr(self):
        self.eat(LBRACE)
        result = self.expr()
        self.eat(RBRACE)
        return result

    def expr(self):
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result -= self.term()

        return result
