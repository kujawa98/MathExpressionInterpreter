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


if __name__ == '__main__':
    unittest.main()
