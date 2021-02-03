import lib
# fractional error vs steps
a = 1
b = 1.5
c = 2
N = 100
E = []
n = []
for i in range(1, 250):
    e = lib.ellipsoid(a, b, c, N*i)
    E.append(e[4])
    n.append(N*i)
# storing data for plot
with open('error.txt', 'w') as file:
    file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n"), file.writelines("\n""\n")
    file.writelines("[")
    file.writelines("%s," % i for i in E)
    file.writelines("]"), file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n")
    file.writelines("[#################################]")
    file.writelines(
        "\n""\n"), file.writelines("\n""\n"), file.writelines("\n""\n")
    file.writelines("[")
    file.writelines("%s," % i for i in n)
    file.writelines("]"), file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n")
