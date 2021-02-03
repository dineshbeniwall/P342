import lib
# Volume vs N
a = 1
b = 1.5
c = 2
N = 100
V = []
n = []
for i in range(1, 500):
    v = lib.ellipsoid(a, b, c, N*i)
    V.append(v[0])
    n.append(N*i)
# storing data for plot
with open('vol.txt', 'w') as file:
    file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n"), file.writelines("\n""\n")
    file.writelines("[")
    file.writelines("%s," % i for i in V)
    file.writelines("]"), file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n")
    file.writelines("[#################################]")
    file.writelines(
        "\n""\n"), file.writelines("\n""\n"), file.writelines("\n""\n")
    file.writelines("[")
    file.writelines("%s," % i for i in n)
    file.writelines("]"), file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n")
