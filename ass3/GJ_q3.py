def matply(M, y):
    a = []
    b = []
    c = []
    product = [a, b, c]
    for rowx, r in zip(M, product):
        j = 0  # columns
        while j != len(y[0]):
            k = 0
            sum = 0
            for rowy in y:
                sum += rowx[k]*rowy[j]
                k += 1
            r.append(sum)
            j += 1
    return product


def augment(a, b):
    for i in range(0, len(a)):
        try:
            for j in range(0, len(b[0])):
                a[i].append(b[i][j])
        except TypeError:
            a[i].append(b[i])
    return a


def partialpivot(a):
    r = len(a)
    for k in range(0, r-1):
        if a[k][k] == 0:
            for i in range(k+1, r):
                if abs(a[i][k]) > abs(a[k][k]):
                    store = a[k]
                    a[k] = a[i]
                    a[i] = store
    return a


def gaussjordan(a, b):
    augment(a, b)
    partialpivot(a)
    row = len(a)
    col = len(a[0])
    for k in range(0, row):
        pivot = a[k][k]
        # for the pivot row divide by akk
        for j in range(k, col):
            a[k][j] = a[k][j]/pivot
        # for the non pivot row
        for i in range(0, row):
            if i == k or a[i][k] == 0:
                continue
            factor = a[i][k]
            # substraction
            for d in range(k, col):
                a[i][d] = a[i][d]-factor * a[k][d]
    return a


def solve(a, b):
    gaussjordan(a, b)
    sol = [[], [], []]
    print("Transformed augmented matrix:", a)
    for i in range(0, len(a)):
        for j in range(len(a), len(a[1])):
            sol[i].append(a[i][j])
    return sol


rows = 3
with open('A.txt') as f:
    a = []
    for i in range(0, rows):
        a.append(list(map(float, f.readline().split())))
with open('A.txt') as f:
    m = []
    for i in range(0, rows):
        m.append(list(map(float, f.readline().split())))
b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

ainv = solve(a, b)
print('A inverse:', ainv)
print('A*Ainv:', matply(m, ainv))
