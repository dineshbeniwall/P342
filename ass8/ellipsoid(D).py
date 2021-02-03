import lib

a = 1
b = 1.5
c = 2
N = 50000
v = lib.ellipsoid(a, b, c, N)

# storing data for plotting
with open('3D.txt', 'w') as file:
    file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n"), file.writelines("\n""\n")
    file.writelines("[")
    file.writelines("%s," % i for i in v[1])
    file.writelines("]"), file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n")
    file.writelines("[#################################]")
    file.writelines(
        "\n""\n"), file.writelines("\n""\n"), file.writelines("\n""\n")
    file.writelines("[")
    file.writelines("%s," % i for i in v[2])
    file.writelines("]"), file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n")
    file.writelines("[#################################]")
    file.writelines(
        "\n""\n"), file.writelines("\n""\n"), file.writelines("\n""\n")
    file.writelines("[")
    file.writelines("%s," % i for i in v[3])
    file.writelines("]"), file.writelines("[#################################]"), file.writelines(
        "\n""\n"), file.writelines("\n""\n")
