""" Insertion sort """
def insertion(array: list):
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