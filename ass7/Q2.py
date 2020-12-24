import math
import lib


# dy/dx=z
def func1(z, x):
    return z


def func2(z, x):
    return 1-x-z


h = 0.5
r1 = lib.rk4(func1, func2, 1, 2, 0, 5.5, h)
h = 0.2
r2 = lib.rk4(func1, func2, 1, 2, 0, 5, h)
h = 0.08
r3 = lib.rk4(func1, func2, 1, 2, 0, 5, h)
h = 0.02
r4 = lib.rk4(func1, func2, 1, 2, 0, 5, h)

# append the answer
with open('q2.txt', 'w') as filehandle:
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r1[0])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r1[1])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r2[0])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r2[1])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r3[0])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r3[1])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r4[0])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r4[1])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
