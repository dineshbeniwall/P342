rows = 3
with open('mat_m.txt') as f:
    M = []
    for i in range(0, rows):
        M.append(list(map(float, f.readline().split())))
with open('N.txt') as f:
    N = []
    for i in range(0, rows):
        N.append(list(map(float, f.readline().split())))
with open('A.txt') as f:
    A = []
    for i in range(0, rows):
        A.append(list(map(float, f.readline().split())))
with open('B.txt') as f:
    B = []
    for i in range(0, rows):
        B.append(list(map(float, f.readline().split())))

# ******************************##
# change variable here for M x N or M x A or M x B....y=A or B or N

y = A


# general matrix multipalication
a = []
b = []
c = []
product = [a, b, c]
try:
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
    print("Matrix multipalication = ", product)
except TypeError:
    for rowx, r in zip(M, product):
        k = 0
        sum = 0
        for rowy in y:
            sum += rowx[k]*rowy
            k += 1
        a.append(sum)
    print("Matrix multipalication = ", a)

# M x N = [[0, 5, 0], [-2, -1, 1], [1, 2, -1]]
# M x A = [[6], [-2], [3]]
# M x B = [[4, -3], [-1, 2], [2, -2]]
