from pascal_intepreter.part10.token import Token


class Lexer:
    def __init__(self, text: str):
        self.text = text

    def get_next_token(self) -> Token:
        raise NotImplemented('TODO: Implement')
