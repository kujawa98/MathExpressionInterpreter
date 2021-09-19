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
        res_node = self.parser_.parse("9")
        nd = Node(NodeType.NUMBER, None, None, 9)
        self.assertIsInstance(res_node, Node)
        self.assertEqual(res_node.type, NodeType.NUMBER)
        self.assertEqual(res_node.value, nd.value)

    def test_more_than_one_number(self):
        res_node = self.parser_.parse("9 91 4")
        self.assertEqual(res_node, None)

    def test_operators_nodes(self):
        res_node = self.parser_.parse("+*/-")
        self.assertEqual(res_node, None)

    def test_simple_exp(self):
        nd = self.parser_.parse("9 + 10")
        self.assertIsInstance(nd, Node)
        self.assertEqual(nd.type, NodeType.ADD)
        self.assertEqual(nd.left_child.type, NodeType.NUMBER)
        self.assertEqual(nd.right_child.type, NodeType.NUMBER)
        self.assertEqual(nd.right_child.value, 9)
        self.assertEqual(nd.left_child.value, 10)

    def test_exp(self):
        nd = self.parser_.parse("2+3*4/8")
        print(nd)
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
