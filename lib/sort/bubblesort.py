""" Bubble sort """
def bubble(array: list):
    tmp = array[:]      # copy
    nPers = 0
    nComp = 0

    "Sorts array in place and returns it."
    for j in range(len(tmp)-1, 0, -1):
        nComp += 1          # for
        for i in range(j):
            nComp += 1      # (sub) for
            if tmp[i] > tmp[i + 1]:
                tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
                nPers += 3
        nComp += 1          # (sub) end for
    nComp += 1              # end for
    return nPers, nComp, tmp