from pascal_intepreter.part7.parser import DIV, MUL, MINUS, PLUS


class NodeVisitor(object):
    """
    Note: The visitor code is decoupled from the AST code
    """

    def visit(self, node):
        # Note: generic -- no need to use multiple if statements,
        # dispatches proper method based on the node type
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Num(self, node):
        return node.value


if __name__ == '__main__':
    from spi import Token, MUL, PLUS, INTEGER, Num, BinOp

    mul_token = Token(MUL, '*')
    plus_token = Token(PLUS, '+')
    mul_node = BinOp(
        left=Num(Token(INTEGER, 2)),
        op=mul_token,
        right=Num(Token(INTEGER, 7))
    )
    add_node = BinOp(
        left=mul_node,
        op=plus_token,
        right=Num(Token(INTEGER, 3))
    )

    interpreter = Interpreter(None)
    print(interpreter.visit(add_node))
