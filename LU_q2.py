import lib
# open file
with open('q2.txt') as f:
    d = []
    for i in range(0, 4):
        d.append(list(map(float, f.readline().split())))
# input of identity matrix
with open('q2i.txt') as f:
    b = []
    for i in range(0, 4):
        b.append(list(map(float, f.readline().split())))

# makeready function does poviting if needed
d = lib.makeready(d)
det = lib.determinant(d)
print("determinant: ", det)
# As determinant is not zero therefor inverse exist

# inverse of given matrix
din = lib.inverse(d, b)
print('Inverse: ', din)
