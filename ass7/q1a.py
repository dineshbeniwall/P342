import math
import lib


def func(x):
    f = math.log(x) - math.sin(x)  # first equation
    return f


print("Root by bisection method: ", lib.bisection(1.5, 2.5, func))
print("Root by regular falsi method: ", lib.regularfalsi(1.5, 2.5, func))
print("Root by newton raphson method: ", lib.newtonraphson(1.5, func))


'''
[Bisection method] root: 2.2191076278686523
[Regular falsi method] root: 2.2191071418525734
[Netwton Raphson method] root: 2.219107148913746
'''
