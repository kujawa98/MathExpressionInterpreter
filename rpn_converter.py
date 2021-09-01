class RPNConverter:
    def jmp_next(self, exp_iter):
        try:
            return next(exp_iter)
        except StopIteration:
            return None

    def to_rpn(self, expression):
        result = []
        if expression:
            exp_iter = iter(expression)
            current_char = self.jmp_next(exp_iter)
            op_stack = []
            while current_char:
                if current_char.isspace():
                    current_char = self.jmp_next(exp_iter)
                    continue
                elif current_char.isdigit():
                    current_digit = ""
                    while current_char != None and current_char.isdigit():
                        current_digit += current_char
                        current_char = self.jmp_next(exp_iter)
                    result.append(current_digit)
                elif current_char in "+-*/":
                    if not op_stack:
                        op_stack.append(current_char)
                    else:
                        while current_char in "+-*/":
                            if op_stack and current_char in "+-" and op_stack[-1] in "+-*/":
                                result.append(op_stack.pop())
                            elif op_stack and current_char in "*/" and op_stack[-1] in "*/":
                                result.append(op_stack.pop())
                            else:
                                op_stack.append(current_char)
                                break
                    current_char = self.jmp_next(exp_iter)
                else:
                    print("Invalid character")
                    return ""
            while op_stack:
                result.append(op_stack.pop())
            return result if result else ""
        return ""
