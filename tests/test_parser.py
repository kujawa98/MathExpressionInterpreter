import unittest
from parser_ import Parser
from tokens import *
from nodes import *


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser_ = Parser()

    def test_empty(self):
        self.assertEqual(self.parser_.parse([]), None)

    def test_one_number(self):
        tk = [Token(TokenType.NUMBER, 9)]
        val = tk[0].value
        res_node = self.parser_.parse(tk)
        nd = Node(NodeType.NUMBER, None, None, val)
        self.assertIsInstance(res_node, Node)
        self.assertEqual(res_node.type, NodeType.NUMBER)
        self.assertEqual(res_node.value, nd.value)

    def test_more_than_one_number(self):
        tkns = [Token(TokenType.NUMBER, 9), Token(TokenType.NUMBER, 91), Token(TokenType.NUMBER, 4)]
        res_node = self.parser_.parse(tkns)
        self.assertEqual(res_node, None)

    def test_operators_nodes(self):
        tkns = [Token(TokenType.ADD), Token(TokenType.MUL), Token(TokenType.DIV), Token(TokenType.SUB)]
        res_node = self.parser_.parse(tkns)
        self.assertEqual(res_node, None)


#         check if there's number in a first place, if so, check if there' any tokens left
#         if so expression is invalid and return None, if not it is OK

if __name__ == '__main__':
    unittest.main()
