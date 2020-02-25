from enum import IntEnum

class SortType(IntEnum):
    Quick = 0
    Bubble = 1
    Insertion = 2
    BinaryTree = 3
    Merge = 4

class RandomType(IntEnum):
    Rand = 10
    Same = 11
    Asc  = 12
    Desc = 13

code_lookup = {
    SortType.Quick: "Quick Sort",
    SortType.Bubble: "Bubble Sort",
    SortType.Insertion: "Insertion Sort",
    SortType.BinaryTree: "Binary Tree Sort",
    SortType.Merge: "Merge Sort",
    
    RandomType.Rand: "Random",
    RandomType.Asc: "Ascending",
    RandomType.Desc: "Descending",
    RandomType.Same: "Same",
}

def key2value(type):
    return code_lookup[type]
