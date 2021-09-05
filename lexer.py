from tokens import *


class Lexer:
    def tokenize(self, expression):
        result = []
        if expression:
            for part in expression:
                if part.isdigit():
                    result.append(Token(TokenType.NUMBER, int(part)))
        return result
