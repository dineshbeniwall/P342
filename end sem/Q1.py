import libraraay
import math


def func(x):
    f = (x-5)*math.exp(x)+5
    return f


# findind the value of x
x = libraraay.newtonraphson(5, func)

h = 6.626e-34
k = 1.381e-23
c = 3e8
# calculating wein's constant
b = h*c/(k*x)


print("Root by newton raphson method: ", libraraay.newtonraphson(5, func))
print("Wein's constant", b)

'''
Root by newton raphson method:  4.965114231744276
Wein's constant 0.0028990103307382923
Absolute error : 0.00000000000216182627 

'''
