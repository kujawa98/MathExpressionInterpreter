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


if __name__ == '__main__':
    unittest.main()
