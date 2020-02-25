""" Quick sort """
def partition(array, left, right): 
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

def _doQuickSort(array, left, right): 
    nPers = 0
    nComp = 0
    if left < right:
        # pivotidx is partitioning index, array[p] is now at right place 
        pivotidx, nPers, cmp = partition(array, left, right)
        
        left = _doQuickSort(array, left, pivotidx-1)
        right = _doQuickSort(array, pivotidx+1, right)

        nPers += left[0] + right[0]
        nComp += 1 + cmp + left[1] + right[1]

    return nPers, nComp, array

def quick(array):
    tmp = array[:]      # copy
    return _doQuickSort(tmp, 0, len(tmp) - 1)