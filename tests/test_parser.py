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
        res_node = self.parser_.parse(tk)
        nd = Node(NodeType.NUMBER, None, None, tk[0].value)
        self.assertIsInstance(res_node, Node)
        self.assertEqual(res_node.type, NodeType.NUMBER)
        self.assertEqual(res_node.value, nd.value)


#         check if there's number in a first place, if so, check if there' any tokens left
#         if so expression is invalid and return None, if not it is OK

if __name__ == '__main__':
    unittest.main()
