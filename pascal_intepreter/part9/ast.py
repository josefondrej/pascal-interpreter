from pascal_intepreter.part9.token import Token


class AST:
    pass


class BinOp(AST):
    def __init__(self, left: AST, op: Token, right: AST):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __repr__(self):
        return f'BinOp({self.left}, {self.token}, {self.right})'

    def __str__(self):
        return self.__repr__()


class Num(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def __repr__(self):
        return f'Num({self.token})'

    def __str__(self):
        return self.__repr__()


class UnaryOp(AST):
    def __init__(self, op: Token, expr: AST):
        self.token = self.op = op
        self.expr = expr

    def __repr__(self):
        return f'UnaryOp({self.token}, {self.expr})'

    def __str__(self):
        return self.__repr__()


class Compound(AST):
    def __init__(self):
        self.children = []

    def __repr__(self):
        return f'Compound({self.children})'

    def __str__(self):
        return self.__repr__()


class Assign(AST):
    def __init__(self, left: AST, op: Token, right: AST):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __repr__(self):
        return f'Assign({self.left}, {self.token}, {self.right})'

    def __str__(self):
        return self.__repr__()


class Var(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def __repr__(self):
        return f'Var({self.token})'

    def __str__(self):
        return self.__repr__()


class NoOp(AST):
    def __repr__(self):
        return 'NoOp()'

    def __str__(self):
        return self.__repr__()
