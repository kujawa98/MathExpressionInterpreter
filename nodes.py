from enum import Enum
from dataclasses import dataclass


class NodeType(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4


@dataclass
class Node:
    type: NodeType
    value: int = None
