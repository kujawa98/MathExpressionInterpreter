from nodes import NodeType


class Interpreter:
    def interpret(self, ast):
        if ast:
            if ast.type == NodeType.NUMBER:
                return ast.value
        return ""
