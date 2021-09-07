import sys
from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser
from rpn_converter import RPNConverter


def main():
    rpn = RPNConverter()
    lex = Lexer()
    par = Parser()
    inter = Interpreter()
    while True:
        exp = input("==> ")
        if exp == 'q':
            sys.exit()
        else:
            r = rpn.to_rpn(exp)
            l = lex.tokenize(r)
            p = par.parse(l)
            print(inter.interpret(p))


if __name__ == "__main__":
    main()
