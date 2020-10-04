import lib

coff = [1, -3, -7, 27, -18]
a = 3
epsilon = 0.000001
a = lib.roots(coff, a, epsilon, 4)

result = []
for i in range(0, len(a)):
    result.append(a[i])
print("Roots of the polynomials are:", result)
