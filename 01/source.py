import sys
sys.path.append("..")   # append local PYTHONPATH

from lib.sort.type import SortType as st
from lib.sort import Sort
from lib.generate.array import Array

if __name__ == "__main__":
    lengths = [10, 20, 40, 80]
    bin = Sort()        # Example: sType=st.BinaryTree, by default is None (not set)
    
    for n in lengths:
        genType = 10
        test = Array.generate(n, genType)
        bin.process(array=test)
        bin.to_report(array=test, genType=genType)