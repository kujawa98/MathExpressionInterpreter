from tokens import *
from rpn_converter import RPNConverter


class Lexer:
    def __init__(self):
        self.rpn_conv = RPNConverter()

    def tokenize(self, expression):
        result = []
        expression = self.rpn_conv.to_rpn(expression)
        if expression:
            for part in expression:
                if part.isdigit():
                    result.append(Token(TokenType.NUMBER, int(part)))
                elif part == "+":
                    result.append(Token(TokenType.ADD))
                elif part == "-":
                    result.append(Token(TokenType.SUB))
                elif part == "*":
                    result.append(Token(TokenType.MUL))
                elif part == "/":
                    result.append(Token(TokenType.DIV))
        return result
