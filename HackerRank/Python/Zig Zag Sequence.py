def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2) - 1
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2

    while a[st] <= a[ed] and st < n - 1:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")
    return


a = [1, 2, 3, 4, 5, 6, 7]  # expecte [1 2 3 7 6 5 4]
n = 7


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2) - 1
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")
    return


a = [1, 2, 3, 4, 5, 6, 7]  # expecte [1 2 3 7 6 5 4]
n = 7
findZigZagSequence(a, n)
