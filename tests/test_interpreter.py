import unittest

from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser
from rpn_converter import RPNConverter


class InterpreterTest(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.lexer = Lexer()
        self.rpn = RPNConverter()
        self.interpreter = Interpreter()

    def test_empty(self):
        ppp = self.parser.parse(self.lexer.tokenize(self.rpn.to_rpn("")))
        res = self.interpreter.interpret(ppp)
        self.assertEqual(res, "")

    def test_one_number(self):
        ppp = self.parser.parse(self.lexer.tokenize(self.rpn.to_rpn("24")))
        res = self.interpreter.interpret(ppp)
        self.assertEqual(res, 24)

if __name__ == '__main__':
    unittest.main()
