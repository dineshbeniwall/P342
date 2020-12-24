import math
import lib


def func1(z, x):
    return z


def func2(x, z):
    return z+1


# high guess
gh = 2
# low guess
gl = 0

e = 2.71828
h = 0.01
# rk4shooting(function1,function2,y1,x1,y0,x0,last X, step,high guess,low guess)
r1 = lib.rk4shooting(func1, func2, 3.4365, 1, 1, 0, 1.7, h, gh, gl)

# append the answer
with open('Q3.txt', 'w') as filehandle:
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r1[0])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r1[1])
    filehandle.writelines("]")
