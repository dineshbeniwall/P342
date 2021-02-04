import math
import libraraay


def func1(v, t):
    return v


def func2(t, v):
    return -9.8


# high guess
gh = 40
# low guess
gl = 30

e = 2.71828
h = 0.01
# rk4shooting(function1,function2,y1,x1,y0,x0,last X, step,high guess,low guess)
r1 = libraraay.rk4shooting(func1, func2, 45, 5, 2, 0, 6, h, gh, gl)
# r1 stored t, y, v values
print("Velocity at launchpad :", r1[2][0])

'''

Velocity at launchpad : 33.033834331337225

'''


# append the answer
with open('Q3.txt', 'w') as filehandle:
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r1[0])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[########################################################")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r1[1])
    filehandle.writelines("]")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[########################################################")
    filehandle.writelines("\n""\n")
    filehandle.writelines("[")
    filehandle.writelines("%s," % i for i in r1[2])
    filehandle.writelines("]")
