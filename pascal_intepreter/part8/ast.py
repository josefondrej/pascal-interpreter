class AST:
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __str__(self):
        return f'({self.left}{self.op.value}{self.right})'


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return f'{self.value}'


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr

    def __str__(self):
        return f'{self.op.value}{self.expr}'
