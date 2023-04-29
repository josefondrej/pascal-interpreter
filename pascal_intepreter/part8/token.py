class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):  # pragma: no cover
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return f'Token({self.type}, {repr(self.value)})'

    def __repr__(self):  # pragma: no cover
        return self.__str__()

    def __hash__(self):
        return hash((self.type, self.value))

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value
