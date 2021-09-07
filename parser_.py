from nodes import *
from tokens import *


class Parser:
    def parse(self, tokens):
        main_node = None
        if tokens:
            main_node = self.create_node(tokens.pop(), tokens)
        if len(tokens) != 0:
            print("Semantic error")
            return
        return main_node

    def create_node(self, current_token, tokens):
        try:
            if current_token.type == TokenType.ADD:
                l_child = self.create_node(tokens.pop(), tokens)
                r_child = self.create_node(tokens.pop(), tokens)
                return Node(NodeType.ADD, l_child, r_child)
            elif current_token.type == TokenType.SUB:
                l_child = self.create_node(tokens.pop(), tokens)
                r_child = self.create_node(tokens.pop(), tokens)
                return Node(NodeType.SUB, l_child, r_child)
            elif current_token.type == TokenType.MUL:
                l_child = self.create_node(tokens.pop(), tokens)
                r_child = self.create_node(tokens.pop(), tokens)
                return Node(NodeType.MUL, l_child, r_child)
            elif current_token.type == TokenType.DIV:
                l_child = self.create_node(tokens.pop(), tokens)
                r_child = self.create_node(tokens.pop(), tokens)
                return Node(NodeType.DIV, l_child, r_child)
            elif current_token.type == TokenType.NUMBER:
                return Node(NodeType.NUMBER, None, None, current_token.value)
        except IndexError:
            return
