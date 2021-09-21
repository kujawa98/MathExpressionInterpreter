import unittest

from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser
from rpn_converter import RPNConverter


class InterpreterTest(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def test_empty(self):
        res = self.interpreter.execute("")
        self.assertEqual(res, "")

    def test_one_number(self):
        res = self.interpreter.execute("24")
        self.assertEqual(res, 24)

    def test_more_than_one_number(self):
        res = self.interpreter.execute("24 31 54")
        self.assertEqual(res, "")

    def test_operators(self):
        res = self.interpreter.execute("*-+/")
        self.assertEqual(res, "")

    def test_simple_exp(self):
        res = self.interpreter.execute("2+2")
        self.assertEqual(res, 4)

    def test_exp(self):
        res = self.interpreter.execute("2+3*4+10/5")
        self.assertEqual(res, 16)


if __name__ == '__main__':
    unittest.main()
