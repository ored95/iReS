""" Insertion sort """
def insertion(array: list):
    tmp = array[:]      # copy
    nPers = 0
    nComp = 0

    for i in range(1, len(tmp)):
        nComp += 1      # for
        key = tmp[i]
        """
        Move elements of array[0..i-1], that are 
        greater than key, to one position ahead 
        of their current position 
        """
        j = i - 1
        nComp += 1      # while
        while j >= 0:
            nComp += 1  # if-else     
            if key < tmp[j]:
                tmp[j + 1] = tmp[j]
                j -= 1
                nPers += 1
            else:
                break
            nComp += 1  # while
        
        if j < 0:
            nComp += 1  # end while

        if j + 1 != i:    
            tmp[j + 1] = key
            nPers += 1
        nComp += 1      # (last) if

    return nPers, nComp + 1, tmp