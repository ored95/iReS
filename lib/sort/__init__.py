from .type import key2value
from .quicksort import quick
from .bubblesort import bubble
from .insertionsort import insertion
from .tree import binaryTree
from .mergesort import merge

class Sort:
    def __init__(self, sType=None):
        self.logs = ""
        self.nPers = None
        self.nComp = None
        self.sortType = sType

    def process(self, array: list):
        times = [
            quick(array),
            bubble(array),
            insertion(array),
            binaryTree(array),
            merge(array)
        ]
        
        self.nPers = [item[0] for item in times]    # just saving
        self.nComp = [item[1] for item in times]

        TAB = '\t'
        self.logs += f"Input : {TAB.join([str(x) for x in array])}\n"
        self.logs += f"Output: {TAB.join([str(x) for x in times[3][2]])}\n"
        self.logs += f"Number of permutations and comparisons:\n"

        if self.sortType is not None:
            self.logs += f"  - {key2value(self.sortType)}: {times[self.sortType][0]}(P)\t{times[self.sortType][1]}(C)\n"
        else:
            for i in range(len(times)):
                self.logs += f"  - {key2value(i)}: \t{times[i][0]}(P)\t{times[i][1]}(C)\n"
        pass
    
    def to_report(self, array, genType, fileName="report.csv"):
        results = []
        # results.append(f"Array: {' '.join([str(x) for x in array])}\n")
        results.append(f"ArrayLength: {len(array)} - ArrayType: {key2value(genType)}\n")
        results.append(f"Type,Permutation,Comparison\n")
        for i in range(len(self.nPers)):
            results.append(f"{key2value(i)},{self.nPers[i]},{self.nComp[i]}\n")
        results.append("\n")

        with open(fileName, "a") as fs:
            fs.writelines(results)