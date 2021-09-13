import sys
from interpreter import Interpreter


def main():
    inter = Interpreter()
    print("Math Expression Interpreter by Qcu")
    print("Press Q to leave")
    while True:
        exp = input("==> ")
        if exp == 'q':
            sys.exit()
        else:
            print(inter.execute(exp))


if __name__ == "__main__":
    main()
