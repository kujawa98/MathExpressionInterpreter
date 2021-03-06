import unittest
import rpn_converter
import lexer
from tokens import TokenType


class LexerTest(unittest.TestCase):
    def setUp(self):
        self.lex = lexer.Lexer()

    def test_empty(self):
        self.assertEqual(self.lex.tokenize(""), [])

    def test_whitespaces(self):
        self.assertEqual(self.lex.tokenize("   \t\n\n\v\r\f\n\t     "), [])

    def test_digits_only(self):
        res = self.lex.tokenize(" 26  4 8 ")
        tkns = [TokenType.NUMBER, TokenType.NUMBER, TokenType.NUMBER]
        self.assertEqual(len(res), len(tkns))
        for i in range(len(tkns)):
            self.assertEqual(res[i].type, tkns[i])

    def test_operators_only(self):
        res = self.lex.tokenize("+-*//*-+")
        tkns = [TokenType.ADD, TokenType.MUL, TokenType.DIV, TokenType.DIV, TokenType.MUL, TokenType.SUB, TokenType.SUB,
                TokenType.ADD]
        self.assertEqual(len(res), len(tkns))
        for i in range(len(tkns)):
            self.assertEqual(res[i].type, tkns[i])

    def test_tokens_types(self):
        exps = ["2+3*7", "6-8/2*41", "6-8"]
        res = list(map(lambda x: self.lex.tokenize(x), exps))
        tkns0 = [TokenType.NUMBER, TokenType.NUMBER, TokenType.NUMBER, TokenType.MUL, TokenType.ADD]
        tkns1 = [TokenType.NUMBER, TokenType.NUMBER, TokenType.NUMBER, TokenType.DIV, TokenType.NUMBER, TokenType.MUL,
                 TokenType.SUB]
        tkns2 = [TokenType.NUMBER, TokenType.NUMBER, TokenType.SUB]
        for i in range(len(res[0])):
            self.assertEqual(res[0][i].type, tkns0[i])
        for i in range(len(res[1])):
            self.assertEqual(res[1][i].type, tkns1[i])
        for i in range(len(res[2])):
            self.assertEqual(res[2][i].type, tkns2[i])

    def test_tokens_values(self):
        exps = ["2+3*7", "6-8/2*41", "6-8"]
        res = list(map(lambda x: self.lex.tokenize(x), exps))
        tkns0 = [2, 3, 7, None, None]
        tkns1 = [6, 8, 2, None, 41, None, None]
        tkns2 = [6, 8, None]
        for i in range(len(res[0])):
            self.assertEqual(res[0][i].value, tkns0[i])
        for i in range(len(res[1])):
            self.assertEqual(res[1][i].value, tkns1[i])
        for i in range(len(res[2])):
            self.assertEqual(res[2][i].value, tkns2[i])


if __name__ == '__main__':
    unittest.main()
