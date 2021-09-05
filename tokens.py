from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    NUMBER = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    LPAR = 6
    RPAR = 7


@dataclass
class Token:
    type: TokenType
    value: int
