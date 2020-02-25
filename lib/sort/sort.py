from .type import SortType

class Sort:
    def __init__(self):
        self.logs = ""

    def process(self, array:list, sType=SortType.Quick):
        TAB = '\t'
        self.logs += f"======== {sType} ========\n"
        self.logs += f"Input : {TAB.join([str(x) for x in array])}\n"

        if sType == SortType.Bubble:
            pass
        elif sType == SortType.Insertion:
            times, _ = self.insertion(array)
        elif sType == SortType.BinaryTree:
            pass
        else:
            pass

        self.logs += f"Output: {TAB.join([str(x) for x in array])}\n"
        self.logs += f"Number of permutations: {times}\n"
    
    def insertion(self, array):
        nPers = 0
        for i in range(1, len(array)):
            key = array[i]
            """
            Move elements of array[0..i-1], that are 
            greater than key, to one position ahead 
            of their current position 
            """
            j = i - 1
            while j >= 0 and key < array[j]: 
                array[j + 1] = array[j]
                nPers += 1
                j -= 1
                
            array[j + 1] = key
        return nPers, array