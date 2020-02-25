import sys
sys.path.append("..")   # append local PYTHONPATH

from lib.sort.type import SortType as st
from lib.sort.sort import Sort

if __name__ == "__main__":
    test = [12, 11, 13, 5, 6, 9, 1, 15, 3, 4, 8]
    bin = Sort()
    bin.process(test)
    print(bin.logs)