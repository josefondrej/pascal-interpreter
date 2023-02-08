from pascal_intepreter.part7.interpreter import NodeVisitor


class InfixToLISPTranslator(NodeVisitor):
    def translate(self, text: str) -> str:
        raise NotImplementedError
