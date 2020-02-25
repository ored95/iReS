""" Bubble sort """
def bubble(array: list):
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