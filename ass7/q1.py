import math
import lib

# function


def func(y, x):
    f = (y*math.log(y))/x
    return f


e = 2.71828
h = 0.5
r1 = lib.euler(func, e, 2, 10, h)
h = 0.1
r2 = lib.euler(func, e, 2, 10, h)
h = 0.01
r3 = lib.euler(func, e, 2, 10, h)
h = 0.02
r4 = lib.euler(func, e, 2, 10, h)

# append the answer
with open('q1a.txt', 'w') as filehandle:
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
