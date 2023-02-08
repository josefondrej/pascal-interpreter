from pascal_intepreter.part7.spi import NodeVisitor, Lexer, Parser

OPERATION_TYPE_TO_STRING = {'PLUS': '+', 'MINUS': '-', 'MUL': '*', 'DIV': '/'}


class InfixToPostfixTranslator(NodeVisitor):
    def visit_BinOp(self, node):
        op_str = OPERATION_TYPE_TO_STRING[node.op.type]
        return f"{self.visit(node.left)} {self.visit(node.right)} {op_str}"

    def visit_Num(self, node):
        return node.value

    def translate(self, text: str) -> str:
        lexer = Lexer(text)
        parser = Parser(lexer)
        tree = parser.parse()
        return self.visit(tree)
