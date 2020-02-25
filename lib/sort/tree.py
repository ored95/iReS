"""
Binary tree implementation in Python
"""
class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, newData):
        nComp = 1
        if self.data:
            nComp += 1
            if self.data <= newData:
                nComp += 1
                if self.right is None:
                    self.right = Tree(newData)
                else:
                    nComp += self.right.insert(newData)
            else:
                nComp += 1
                if self.left is None:
                    self.left = Tree(newData)
                else:
                    nComp += self.left.insert(newData)
        else:
            self.data = newData
        
        return nComp

    def pop(self, lst):
        nComp = 0
        if self.left:
            nComp += 1 + self.left.pop(lst)
        lst.append(self.data),
        if self.right:
            nComp += 1 + self.right.pop(lst)
        return nComp
            
def _doBinaryTreeSort(array: list):
    nPers = 2 * len(array)
    nComp = 0
    bTree = Tree(array[0])
    for i in range(1, len(array)):
        nComp += 1 + bTree.insert(array[i]) # for
    nComp += 1      # end for

    array = []
    nComp += bTree.pop(array)
    return nPers, nComp, array

""" Binary Tree Sort """
def binaryTree(array: list):
    tmp = array[:]      # copy
    return _doBinaryTreeSort(tmp)