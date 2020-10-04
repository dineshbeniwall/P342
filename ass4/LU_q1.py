# import library
import lib
# open a and b
with open('q1a.txt') as f:
    a = []
    for i in range(0, 4):
        a.append(list(map(float, f.readline().split())))
opn = open('q1b.txt', 'r')
lsplit = opn.readline().split()
b = []
for val in lsplit:
    b.append(float(val))

# upper triangle matrix
ut = lib.ludecom(a)[1]
print('Upper triangle matrix: ', ut)
# lower triangle matrix
lt = lib.ludecom(a)[0]
print('Lower triangle matrix: ', lt)
# AX=B      LUX=B   LZ=B   UX=Z
# Z
z = lib.forback(a, b)[0]
# x or solution of given linear equations
x = lib.forback(a, b)[1]
print('Solution matrix ', x)
for i in range(0, len(x)):
    print('X', i+1, '=', x[i])
