from enum import Enum
from dataclasses import dataclass


class NodeType(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    NUMBER = 5


@dataclass
class Node:
    type: NodeType
    left_child: any
    right_child: any
    value: int = None
