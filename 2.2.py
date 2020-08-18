# Create two vectors of type A=(a1,a2,a3) and B=(b1,b2,b3) with numbers of your
# choice in the code itself. Find A+B and A.B (dot product).
A = [1, 2, 3]
B = [7, 8, 9]

sum = []
dot = 0
for i, j in zip(A, B):
    sum.append(i+j)
    dot += i*j
print("A+B", sum)
# [8, 10, 12]
print("A.B =", dot)
# 50
