import unittest
import rpn_converter
import lexer
from tokens import TokenType


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.rpn_conv = rpn_converter.RPNConverter()
        self.lex = lexer.Lexer()

    def test_empty(self):
        exp = self.rpn_conv.to_rpn("")
        self.assertEqual(self.lex.tokenize(exp), [])

    def test_whitespaces(self):
        exp = self.rpn_conv.to_rpn("   \t\n\n\v\r\f\n\t     ")
        self.assertEqual(self.lex.tokenize(exp), [])

    def test_digits_only(self):
        exp = self.rpn_conv.to_rpn(" 26  4 8 ")
        res = self.lex.tokenize(exp)
        tkns = [TokenType.NUMBER, TokenType.NUMBER, TokenType.NUMBER]
        self.assertEqual(len(res), len(tkns))
        for i in range(len(tkns)):
            self.assertEqual(res[i].type, tkns[i])

    def test_operators_only(self):
        exp = self.rpn_conv.to_rpn("+-*//*-+")
        res = self.lex.tokenize(exp)
        tkns = [TokenType.ADD, TokenType.MUL, TokenType.DIV, TokenType.DIV, TokenType.MUL, TokenType.SUB, TokenType.SUB,
                TokenType.ADD]
        self.assertEqual(len(res), len(tkns))
        for i in range(len(tkns)):
            self.assertEqual(res[i].type, tkns[i])

    def test_tokens_types(self):
        exps = list(map(lambda x: self.rpn_conv.to_rpn(x), ["2+3*7", "6-8/2*41", "6-8"]))
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


if __name__ == '__main__':
    unittest.main()
