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

    def test_simple_exp(self):
        tkns = [Token(TokenType.NUMBER, 9), Token(TokenType.NUMBER, 10), Token(TokenType.ADD)]
        nd = self.parser_.parse(tkns)
        self.assertIsInstance(nd, Node)
        self.assertEqual(nd.type, NodeType.ADD)
        self.assertEqual(nd.left_child.type, NodeType.NUMBER)
        self.assertEqual(nd.right_child.type, NodeType.NUMBER)
        self.assertEqual(nd.right_child.value, 9)
        self.assertEqual(nd.left_child.value, 10)

    def test_exp(self):
        tkns = [Token(TokenType.NUMBER, 2), Token(TokenType.NUMBER, 3), Token(TokenType.NUMBER, 4),
                Token(TokenType.MUL), Token(TokenType.NUMBER, 8), Token(TokenType.DIV), Token(TokenType.ADD)]
        nd = self.parser_.parse(tkns)
        self.assertEqual(nd.right_child.type, NodeType.NUMBER)
        self.assertEqual(nd.right_child.value, 2)
        self.assertEqual(nd.left_child.type, NodeType.DIV)
        self.assertEqual(nd.left_child.left_child.type, NodeType.NUMBER)
        self.assertEqual(nd.left_child.left_child.value, 8)
        self.assertEqual(nd.left_child.right_child.type, NodeType.MUL)
        self.assertEqual(nd.left_child.right_child.left_child.value, 4)
        self.assertEqual(nd.left_child.right_child.right_child.value, 3)


if __name__ == '__main__':
    unittest.main()
