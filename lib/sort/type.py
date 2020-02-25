from enum import IntEnum

class SortType(IntEnum):
    Quick = 0
    Bubble = 1
    Insertion = 2
    BinaryTree = 3

code_lookup = {
    SortType.Quick: "Quick Sort",
    SortType.Bubble: "Bubble Sort",
    SortType.Insertion: "Insertion Sort",
    SortType.BinaryTree: "Binary Tree Sort"
}

def key2value(type:SortType):
    return code_lookup[type]