def _doMergeSort(array: list):
    nPers = 0
    nComp = 0
    if len(array) > 1:
        mid = len(array) // 2
        leftPart = array[:mid]
        rightPart = array[mid:]

        left = _doMergeSort(leftPart)
        right = _doMergeSort(rightPart)

        nPers += left[0] + right[0]
        nComp += 1 + left[1] + right[1]     # if
        
        i = 0
        j = 0
        k = 0

        nComp += 1      # while
        while i < len(leftPart):
            nComp += 1 + 1      # while + if-else
            if j < len(rightPart):
                if leftPart[i] <= rightPart[j]:
                    array[k] = leftPart[i]
                    i += 1
                else:
                    array[k] = rightPart[j]
                    j += 1
                k += 1
                nPers += 1
                nComp += 1      # (sub)if-else
            else:
                break
        
        nComp += 1      # while
        while i < len(leftPart):
            array[k] = leftPart[i]
            i += 1
            k += 1
            nPers += 1
            nComp += 1  # while
        
        nComp += 1      # while
        while j < len(rightPart):
            array[k] = rightPart[j]
            j += 1
            k += 1
            nPers += 1
            nComp += 1  # while

    return nPers, nComp, array

def merge(array: list):
    tmp = array[:]      # copy
    return _doMergeSort(tmp)