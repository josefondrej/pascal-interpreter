from enum import Enum


class TokenType(Enum):
    INTEGER = 'INTEGER'
    PLUS = 'PLUS'
    EOF = 'EOF'  # EOF (end-of-file) token is used to indicate that there is no more input left for lexical analysis
