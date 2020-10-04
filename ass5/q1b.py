import math
import lib


def func(x):
    f = -x - math.cos(x)  # second equation
    return f


print("Root by bisection method: ", lib.bisection(1.5, 2.5, func))
print("Root by regular falsi method: ", lib.regularfalsi(1.5, 2.5, func))
print("Root by newton raphson method: ", lib.newtonraphson(2.5, func))

'''
[Bisection method] root: -0.739084780216217
[Regular falsi method] root: -0.7390851319823046
[Netwton Raphson method] root: -0.7390850544025488
'''
