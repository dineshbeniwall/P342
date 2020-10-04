# Polynomial function. Input coff and value of x
import math


def polynomial(coff, x):
    # order of polynomial
    n = len(coff)-1
    p = 0
    for i in range(0, len(coff)):
        p = coff[i]*x**(n-i)+p
    return p


# polynomial synthetic division
def polydivide(coff, d):
    ncoff = []
    ncoff.append(coff[0])
    i = 0
    for i in range(0, len(coff)-2):
        ncoff.append(ncoff[i]*d+coff[i+1])
    return ncoff


# differentiation of polynomial
def differentiation(coff, x):
    h = 0.0001
    fd = (polynomial(coff, x+h)-polynomial(coff, x-h))/(2*h)
    return fd


# double differentiation of polynomial
def doublediff(coff, x):
    h = 0.0001
    fdd = (differentiation(coff, x+h)-differentiation(coff, x-h))/(2*h)
    return fdd


# Roots of polynomial
# input coff. of polynomial, alpha0=initial guess, epsilon, n=order of polynomial
def roots(coff, alpha0, epsilon, n):
    root = []
    alphai = alpha0
    for i in range(0, n):
        alphaii = 0
        if polynomial(coff, alpha0) < epsilon:
            root.append(alphai)
            coff = polydivide(coff, alphai)
        else:
            while abs(alphaii-alphai) > epsilon:
                p = polynomial(coff, alphai)
                pi = differentiation(coff, alphai)
                pii = doublediff(coff, alphai)
                g = pi/p
                h = g**2-pii/p
                d1 = g+((n-1)*(n*h-g**2))**(1/2)
                d2 = g-((n-1)*(n*h-g**2))**(1/2)
                if abs(d1) > abs(d2):
                    a = n/d1
                else:
                    a = n/d2
                alphaii = alphai-a
                alphai = alphaii
            root.append(alphai)
            coff = polydivide(coff, alphai)
        # print(coff, alphai)
    return root


# Bracketing the root
def bracketing(f, a):
    fa = f(a[0])
    fb = f(a[1])
    beta = 0.7
    for i in range(0, 12):
        if fa * fb < 0:
            return True
        if fa * fb > 0:
            if(abs(fa) < abs(fb)):
                a[0] = a[0] - beta * (a[1] - a[0])
            elif(abs(fa) > abs(fb)):
                a[1] = a[1] + beta * (a[1] - a[0])
    if fa * fb < 0:
        return True
    else:
        return False


# Bisection method for roots, where f is function and a is guess values
def bisection(f, a):
    epsilon = pow(10, -6)
    if (bracketing(f, a)):
        for i in range(0, 200):
            c = (a[0] + a[1]) / 2
            if f(a[0]) * f(c) < 0:
                a[1] = c
            elif f(a[0]) * f(c) > 0:
                a[0] = c
            elif f(a[0]) * f(c) == 0:
                if abs(f(c)) == 0:
                    print("The root is", c)
                    return True
                elif(abs(f(a[0])) == 0):
                    print("The root is", a[0])
                    return True
            file = open("Q1_bisection.txt", 'w')
            file.write("%i         %5.21f\n" % (i+1, abs(a[1]-a[0])))
            file.close()
            if (abs(a[1] - a[0]) < epsilon):
                return True
    else:
        print("Try some other values for guess")
        return False


# False Position method for roots, where f is function and a is guess values
def regularfalsi(f, a):
    epsilon = pow(10, -6)
    z = 0
    if (bracketing(f, a)):
        for i in range(200):
            if i != 0:
                z = c
            c = a[1] - (((a[1] - a[0]) * f(a[1])) / (f(a[1]) - f(a[0])))
            if f(a[0]) * f(c) < 0:
                a[1] = c
            elif f(a[0]) * f(c) > 0:
                a[0] = c
            elif f(a[0]) * f(c) == 0:
                if abs(f(c)) == 0:
                    print("The root is", c)
                    return True
                elif abs(f(a[0])) == 0:
                    print("The root is", a[0])
                    return True
            file = open("Q1_regular_falsi.txt", 'w')
            file.write("%i         %5.21f\n" % (i+1, abs(z - c)))
            file.close()
            if i != 0:
                if abs(z - c) < epsilon:
                    a[1] = c
                    return True
    else:
        print("Try some other values for guess")
        return False


# differentiation of function
def Diffrentiation(f, x):
    h = math.pow(10, -4)
    return ((f(x + h) - f(x - h)) / (2 * h))


# Newton Raphson method for roots
def newtonraphson(f, x):
    x1 = x
    epsilon = pow(10, -6)
    for i in range(200):
        n = f(x1)
        m = Diffrentiation(f, x1)
        x1 = x1 - (n / m)
        file = open("Q1_newtonraphson.txt", 'w')
        file.write("%i         %5.21f\n" % (i + 1, abs(x1 - x)))
        file.close()
        if abs(x1 - x) < epsilon:
            return x1
        x = x1
