def quicksort(m):
    quicksort2(m, 0, len(m) - 1)


def quicksort2(m, low, hi):
    threshold = 20
    if hi - low < threshold and low < hi:
        quick_selection(m, low, hi)
    elif low < hi:
        p = partition(m, low, hi)
        quicksort2(m, low, p - 1)
        quicksort2(m, p + 1, hi)


def getpivot(m, low, hi):
    mid = (hi + low) // 2
    s = sorted([m[low], m[mid], m[hi]])
    if s[1] == m[low]:
        return low
    elif s[1] == m[mid]:
        return mid
    return hi


def partition(m, low, hi):
    pivotIndex = getpivot(m, low, hi)
    pivotValue = m[pivotIndex]
    m[pivotIndex], m[low] = m[low], m[pivotIndex]
    border = low

    for i in range(low, hi + 1):
        if m[i] < pivotValue:
            border += 1
            m[i], m[border] = m[border], m[i]
    m[low], m[border] = m[border], m[low]
    return border


def quickselection(x, first, last):
    for i in range(first, last):
        minIndex = i
        for j in range(i + 1, last + 1):
            if x[j] < x[minIndex]:
                minIndex = j
        if minIndex != i:
            x[i], x[minIndex] = x[minIndex], x[i]
