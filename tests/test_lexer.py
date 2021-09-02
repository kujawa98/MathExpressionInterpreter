import unittest
import rpn_converter
import lexer


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

if __name__ == '__main__':
    unittest.main()
