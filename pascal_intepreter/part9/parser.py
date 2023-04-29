from typing import List

from pascal_intepreter.part9.ast import AST, Compound, Assign, Var, NoOp, BinOp, Num, UnaryOp
from pascal_intepreter.part9.lexer import Lexer
from pascal_intepreter.part9.token_type import DOT, SEMI, ID, ASSIGN, PLUS, MINUS, MUL, DIV, RPAREN, LPAREN, \
    INTEGER, BEGIN, END


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def factor(self):
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOp(op=token, expr=self.factor())
            return node
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOp(op=token, expr=self.factor())
            return node
        elif token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            node = self.variable()
            return node

    def term(self):
        node = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def empty(self) -> AST:
        return NoOp()

    def variable(self) -> AST:
        node = Var(self.current_token)
        self.eat(ID)
        return node

    def assignment_statement(self) -> AST:
        left = self.variable()
        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def statement(self) -> AST:
        if self.current_token.type == BEGIN:
            node = self.compound_statement()
        elif self.current_token.type == ID:
            node = self.assignment_statement()
        else:
            node = self.empty()
        return node

    def statement_list(self) -> List[AST]:
        node = self.statement()
        results = [node]

        while self.current_token.type == SEMI:
            self.eat(SEMI)
            results.append(self.statement())

        return results

    def compound_statement(self) -> Compound:
        self.eat(BEGIN)
        nodes = self.statement_list()
        self.eat(END)

        root = Compound()
        for node in nodes:
            root.children.append(node)
        return root

    def eat(self, token_type: str):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def program(self) -> AST:
        node = self.compound_statement()
        self.eat(DOT)
        return node

    def error(self):
        raise Exception('Invalid syntax')

    def parse(self) -> AST:
        node = self.program()
        if self.current_token.type != 'EOF':
            self.error()
        return node
