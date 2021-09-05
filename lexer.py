from tokens import *


class Lexer:
    def tokenize(self, expression):
        result = []
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
