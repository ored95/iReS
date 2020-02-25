from .type import *
import random

class Sort:
    def __init__(self, sType=None):
        self.logs = ""
        self.nPers = None
        self.nComp = None
        self.sortType = sType

    def process(self, array: list, ):
        times = [
            self.quick(array),
            self.bubble(array),
            self.insertion(array),
            self.binaryTree(array)
        ]
        
        self.nPers = [item[0] for item in times]    # just saving
        self.nComp = [item[1] for item in times]

        TAB = '\t'
        self.logs += f"Input : {TAB.join([str(x) for x in array])}\n"
        self.logs += f"Output: {TAB.join([str(x) for x in times[0][2]])}\n"
        self.logs += f"Number of permutations and comparisons:\n"

        if self.sortType is not None:
            self.logs += f"\t{key2value(self.sortType)}: {times[self.sortType][0]}(P)\t{times[self.sortType][1]}(C)\n"
        else:
            for i in range(0, len(times)):
                self.logs += f"  - {key2value(i)}: \t{times[i][0]}(P)\t{times[i][1]}(C)\n"
        pass


    """ Quick sort """
    def partition(self, array, left, right): 
        i = left - 1
        pivot = array[right]    # pivot
        nPers = 0
        nComp = 0
        
        for j in range(left, right):
            if array[j] <= pivot:
                i += 1          # increment index of smaller element
                array[i], array[j] = array[j], array[i]
                nPers += 3
                nComp += 1
    
        array[i+1], array[right] = array[right], array[i+1]
        return i + 1, nPers + 3, nComp

    def quick_help(self, array, left, right): 
        nPers = 0
        nComp = 0
        if left < right:
            # pivotidx is partitioning index, array[p] is now at right place 
            pivotidx, nPers, cmp = self.partition(array, left, right)
            
            left = self.quick_help(array, left, pivotidx-1)
            right = self.quick_help(array, pivotidx+1, right)

            nPers += left[0] + right[0]
            nComp += 1 + cmp + left[1] + right[1]

        return nPers, nComp, array

    def quick(self, array):
        tmp = array[:]      # copy
        return self.quick_help(tmp, 0, len(tmp) - 1)


    """ Bubble sort """
    def bubble(self, array: list):
        tmp = array[:]      # copy
        nPers = 0
        nComp = 0

        "Sorts array in place and returns it."
        for j in range(len(tmp)-1, 0, -1):
            for i in range(j):
                if tmp[i] > tmp[i + 1]:
                    tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
                    nPers += 3
                    nComp += 1
        
        return nPers, nComp, tmp

   
    """ Insertion sort """
    def insertion(self, array: list):
        tmp = array[:]      # copy
        nPers = 0
        nComp = 0

        for i in range(1, len(tmp)):
            key = tmp[i]
            """
            Move elements of array[0..i-1], that are 
            greater than key, to one position ahead 
            of their current position 
            """
            j = i - 1
            while j >= 0:
                nComp += 1
                if key < tmp[j]:
                    tmp[j + 1] = tmp[j]
                    j -= 1
                    nPers += 1
                    nComp += 1
                else:
                    break
                
            tmp[j + 1] = key
            nPers += 1
        return nPers, nComp, tmp


    """ Binary Tree Sort """
    def binaryTree(self, array: list):
        tmp = array[:]      # copy
        nPers = 0
        nComp = 0


        
        return nPers, nComp, tmp