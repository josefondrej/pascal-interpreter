from pascal_intepreter.part10.parser import Parser


class Interpreter:
    def __init__(self, parser: Parser):
        self.parser = parser
        self.GLOBAL_SCOPE = dict()

    def interpret(self):
        raise NotImplemented('TODO: Implement')
