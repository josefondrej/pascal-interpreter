from pascal_intepreter.part7.spi import NodeVisitor


class InfixToPostfixTranslator(NodeVisitor):
    def translate(self, text: str) -> str:
        raise NotImplementedError
