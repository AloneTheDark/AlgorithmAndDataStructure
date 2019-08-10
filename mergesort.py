def mergesort(m):
    mergesort2(m, 0, len(m) - 1)


def mergesort2(m, first, last):
    if first < last:
        middle = (first + last) // 2
        mergesort2(m, first, middle)
        mergesort2(m, middle + 1, last)
        merge(m, first, middle, last)


def merge(m, first, middle, last):
    L = m[first:middle + 1]
    R = m[middle + 1:last + 1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = j = 0

    for k in range(first, last + 1):
        if L[i] <= R[j]:
            m[k] = L[i]
            i += 1
        else:
            m[k] = R[j]
            j += 1

