# one way of doing without augmentation
# augmentation is done in question 3
def partialpivot(a, b):
    r = len(b)
    for k in range(0, r-1):
        if a[k][k] == 0:
            for i in range(k+1, r):
                if abs(a[i][k]) > abs(a[k][k]):
                    store = a[k]
                    a[k] = a[i]
                    a[i] = store
                    store = b[k]
                    b[k] = b[i]
                    b[i] = store
    return a, b


def gaussjordan(a, b):
    partialpivot(a, b)
    r = len(b)
    for k in range(0, r):
        pivot = a[k][k]
        # for the pivot row divide by akk
        for j in range(k, r):
            a[k][j] = a[k][j]/pivot
        b[k] = b[k]/pivot
        # for the non pivot row
        for i in range(0, r):
            if i == k or a[i][k] == 0:
                continue
            factor = a[i][k]
            # substraction
            for d in range(k, r):
                a[i][d] = a[i][d]-factor * a[k][d]
            b[i] = b[i]-factor * b[k]
    return a, b


# a = [[0, 2, 0, 1], [2, 2, 3, 2], [4, -3, 0, 1], [6, 1, -6, -5]]
# b = [0, -2, -7, 6]

# ******Question 1******
print('Question 1: \n')
opn = open('bq1.txt', 'r')
lsplit = opn.readline().split()
b = []
for val in lsplit:
    b.append(float(val))
rows = 3
with open('aq1.txt') as f:
    a = []
    for i in range(0, rows):
        a.append(list(map(float, f.readline().split())))
print('a matrix: ', a)
print('b matrix: ', b)
gaussjordan(a, b)
print('Transformed identity: a matrix', a)
print('Solution: b matrix', b)

# ******Question 2******
print('\nQuestion 2: \n')
opn = open('bq2.txt', 'r')
lsplit = opn.readline().split()
b = []
for val in lsplit:
    b.append(float(val))
rows = 3
with open('aq2.txt') as f:
    a = []
    for i in range(0, rows):
        a.append(list(map(float, f.readline().split())))
a = [[0, 2, 5], [3, -1, 2], [1, -1, 3]]
b = [1, -2, 3]
print('a matrix: ', a)
print('b matrix: ', b)
gaussjordan(a, b)
print('Transformed identity: a matrix', a)
print('Solution: b matrix', b)
