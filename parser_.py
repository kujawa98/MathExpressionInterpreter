from nodes import *
from tokens import *


class Parser:
    def parse(self, tokens):
        if len(tokens) == 1 and tokens[0].type == TokenType.NUMBER:
            return Node(NodeType.NUMBER, None, None, tokens[0].value)
        main_node = None
        if tokens:
            return
        return
