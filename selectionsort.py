def selection_sort(m):
    for i in range(0, len(m) - 1):
        minIndex = i
        for j in range(i + 1, len(m)):
            if m[j] < m[minIndex]:
                minIndex = j
        if minIndex != i:
            m[i], m[minIndex] = m[minIndex], m[i]


m = [5, 9, 1, 2, 4, 8, 6, 3, 7]
print(m)
selection_sort(m)
print(m)