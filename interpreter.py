from nodes import NodeType
from parser_ import Parser


class Interpreter:
    def __init__(self):
        self.parser = Parser()

    def execute(self, expression):
        ast = self.parser.parse(expression)
        if ast:
            if ast.type == NodeType.NUMBER:
                return ast.value
            return self.get_value(ast)
        return ""

    def get_value(self, node):
        if node.type == NodeType.ADD:
            return self.get_value(node.right_child) + self.get_value(node.left_child)
        elif node.type == NodeType.SUB:
            return self.get_value(node.right_child) - self.get_value(node.left_child)
        elif node.type == NodeType.MUL:
            return self.get_value(node.right_child) * self.get_value(node.left_child)
        elif node.type == NodeType.DIV:
            return self.get_value(node.right_child) // self.get_value(node.left_child)
        elif node.type == NodeType.NUMBER:
            return node.value
