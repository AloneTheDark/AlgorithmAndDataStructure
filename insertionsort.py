def insertionsort1(m):
    for i in range(1, len(m)):
        for j in range(i - 1, -1, -1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
            else:
                break

def insertionsort2(m):
    for i in range(1, len(m)):
        j = i - 1
        while m[j] > m[j + 1] and j >= 0:
            m[j], m[j + 1] = m[j + 1], m[j]
            j -= 1


# optimized
def insertionsort3(m):
    for i in range(1, len(m)):
        curNum = m[i]
        k = 0
        for j in range(i - 1, -2, -1):
            k = j
            if m[j] > curNum:
                m[j + 1] = m[j]
            else:
                break
        m[k + 1] = curNum
