from pascal_intepreter.part8.ast import AST, BinOp, UnaryOp, Num
from pascal_intepreter.part8.token_type import EOF, PLUS, MINUS, MUL, DIV, INTEGER, LPAREN, RPAREN


class Parser:
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

    def factor(self) -> AST:
        """
        factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN
        """
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            return UnaryOp(op=token, expr=self.factor())
        elif token.type == MINUS:
            self.eat(MINUS)
            return UnaryOp(op=token, expr=self.factor())
        elif token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

    def term(self):
        """
        term   : factor ((MUL | DIV) factor)*
        """
        node = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self) -> AST:
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self) -> AST:
        node = self.expr()
        if self.current_token.type != EOF:
            self.error()
        return node
