import math
import lib


def function(x):
    return (- x - math.cos(x))


a = [-1.3, 0.3]

if(lib.bisection(function, a)):
    print("Root using bisection method : ", ((a[1] + a[0]) / 2), " +/- ", pow(10, -6)/2)

b = [-1.3, 0.3]
if(lib.regularfalsi(function, b)):
    print("Root using Regular Falsi : ", b[1], " +/- ", pow(10, -6))

x = -1.2
print("Root using Newton Raphson : ", lib.newtonraphson(function, x))