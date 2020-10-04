import math
import lib


def function(n):
    return (math.log(n) - math.sin(n))


a = [1.5, 3]

if(lib.bisection(function, a)):
    print("Root using bisection method : ", (abs(a[1] + a[0]) / 2), " +/- ", pow(10, -6)/2)

b = [1.5, 2.5]
if(lib.regularfalsi(function, b)):
    print("Root using Regular Falsi : ", b[1], " +/- ", pow(10, -6))

x = 1.5
print("Root using Newton Raphson : ", lib.newtonraphson(function, x))
