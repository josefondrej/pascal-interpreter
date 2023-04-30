from pascal_intepreter.part10.ast import AST
from pascal_intepreter.part10.lexer import Lexer


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer

    def parse(self) -> AST:
        raise NotImplemented('TODO: Implement')
