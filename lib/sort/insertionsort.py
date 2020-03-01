""" Insertion sort """
def insertion(array: list):
    tmp = array[:]      # copy
    nPers = 0
    nComp = 0

    for i in range(1, len(tmp)):
        j = i - 1
        nComp += 1
        while j >= 0 and tmp[j + 1] < tmp[j]:
            if j == i - 1:
                nComp -= 1
                
            tmp[j + 1], tmp[j] = tmp[j], tmp[j + 1]
            nPers += 1

            j -= 1
            nComp += 1
        
    return nPers, nComp, tmp