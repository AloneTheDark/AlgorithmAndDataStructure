def bubble_sort(m):
    for i in range(0, len(m) - 1):
        done = True
        for j in range(0, len(m) - i - 1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
                done = False
        if done:
            return


m = [5, 9, 1, 2, 4]
print(m)
bubble_sort1(m)
print(m)