import math
import random


# Midpoint / Rectangle method
def midpoint(a, b, n, f):
    # divide integration range in N equal parts
    h = (b-a)/n
    Mn = 0
    dxmax = 0
    for i in range(0, n):
        # midpoint of each intervals
        x = ((a+i*h)+(a+(i+1)*h))/2
        Mn += h*f(x)
        # double differentiation for error
        fddx = ddx(f, x)
        if abs(fddx) > dxmax:
            dxmax = abs(fddx)
    # max error
    er = (((b-a)**3)/(24*(n**2)))*dxmax
    return Mn, er


# Trapezoidal rule
def trapezoidal(a, b, n, f):
    # divide integration range in N equal parts
    h = (b-a)/n
    Tn = 0
    x0 = a
    xpre = x0
    dxmax = 0
    for i in range(1, n+1):
        # endpoint of each intervals
        xi = x0+i*h
        Tn += (h/2)*(f(xpre)+f(xi))
        xpre = xi
        # double differentiation for error
        fddx = ddx(f, xi)
        if abs(fddx) > dxmax:
            dxmax = abs(fddx)
    # max error
    er = (((b-a)**3)/(12*(n**2)))*dxmax
    return Tn, er


# Simpson's rule
def simpson(a, b, n, f):
    # divide integration range in 2N equal
    # this will make our intergral independent of N be even or odd
    h = (b-a)/(2*n)
    S = 0
    dxmax = 0
    # odd terms
    for i in range(1, n+1):
        x = h*(-1+2*i)+a
        S += 4*f(x)
        # fourth order differentiation for error
        fddx = ddddx(f, x)
        if abs(fddx) > dxmax:
            dxmax = abs(fddx)
    # even terms
    for i in range(1, n):
        x = 2*h*i+a
        S += 2*f(x)
        fddx = ddddx(f, x)
        if abs(fddx) > dxmax:
            dxmax = abs(fddx)
    # integral
    Sn = (h/3)*(f(a)+f(b)+S)
    # max error
    er = (((b-a)**5)/(180*(n**4)))*dxmax
    return Sn, er


# Montecarlo integration
def montecarlo(a, b, n, f):
    Fn = 0
    sigmaf = 0
    for i in range(1, n+1):
        # random number
        x = a+(b-a)*random.random()
        # intergral
        Fn += ((b-a)/n)*f(x)
        # error
        sigmaf += math.sqrt(((1/n)*(f(x)**2))-(((1/n)*f(x))**2))
    return Fn, sigmaf


'''#############################################################################'''
'''#############################################################################'''


# double differentiation
def ddx(f, x):
    h = 0.00001
    fddx = (f(x+h)+f(x-h)-2*f(x))/(h**2)
    return fddx


# fourth order differentiation
def ddddx(f, x):
    h = 0.00001
    fddddx = (ddx(f, x+h)+ddx(f, x-h)-2*ddx(f, x))/(h**2)
    return fddddx


# Polynomial function. Input coff and value of x


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


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# bracketing of roots :
def bracketing(a, b, func):
    i = 0
    while i < 12:  # Limiting no.of iterations to 12
        if func(a) * func(b) < 0:
            return a, b
        elif func(a) * func(b) == 0:
            if func(a) == 0:
                print("root of the equation:", a)
            if func(b) == 0:
                print("root of the equation:", b)
        elif func(a) * func(b) > 0:
            if abs(func(a)) < abs(func(b)):
                a = a - 1.5 * (b - a)
            else:
                b = b + 1.5 * (b - a)
        i += 1
    if i > 12:
        print("Iterations are more than 12, try another guess")
    else:
        return a, b


# Bisection method for roots
def bisection(a, b, func):
    file = open('Q1_bisection.txt', 'w')
    a, b = bracketing(a, b, func)  # Recalling the function
    i = 1
    file.write(color.BOLD + "Bisection method" + color.END + "\n{:>3}       {:>10} ".format("Iterations",
                                                                                            "Absolute error") + "\n")
    while abs(a - b) > 0.000001 and i < 200:
        c = (a + b) / 2
        if func(a) * func(c) < 0:
            file.write("{:>3}         {:>10.20f} ".format(i, abs(c - b)) + "\n")
            b = c
        elif func(a) * func(c) > 0:
            file.write("{:>3}         {:>10.20f} ".format(i, abs(c - a)) + "\n")
            a = c
        else:
            print("While iterating through the points one of the point has landed on the root of the equation.")
            print(a, b)
            break
        i += 1
    file.close()
    return b


# regular falsi method for roots
def regularfalsi(a, b, func):
    file = open('Q1_regular_falsi.txt', 'w')
    bracketing(a, b, func)
    i = 1
    file.write(color.BOLD + "False Position method." + color.END + "\n{:>3}       {:>10} ".format("Iterations",
                                                                                                  "Absolute error") + "\n")
    c = 1
    c_n1 = a
    while abs(c - c_n1) > 0.000001 and i < 200:
        c = b - ((b - a) * func(b)) / (func(b) - func(a))
        if func(a) * func(c) < 0:
            c_n1 = b
            file.write("{:>3}         {:>10.20f} ".format(i, abs(c - c_n1)) + "\n")
            b = c
        elif func(a) * func(c) > 0:
            c_n1 = a
            file.write("{:>3}         {:>10.20f} ".format(i, abs(c - c_n1)) + "\n")
            a = c
        else:
            if func(a) == 0:
                print(a, " is the root.")
            elif func(b) == 0:
                print(b, " is the root.")
        i += 1
    file.write("{:>3}         {:>10.20f} ".format(i, abs(c - c_n1)) + "\n")
    file.close()
    return c


# Newton raphson method
def newtonraphson(x_o, func):
    file = open('Q1_Newton_Raphson.txt', 'w')
    h = 0.01
    der = (func(x_o+h) - func(x_o-h))/(2*h)  # Derivative of the function
    x = x_o - (func(x_o) / der)
    copy = 1
    i = 1
    file.write(color.BOLD + "Newton-Raphson method." + color.END + "\n{:>3}       {:>10} ".format("Iterations",
                                                                                                  "Absolute error") + "\n")
    while abs(x - copy) > 0.000001 and i < 200:
        copy = x
        x_o = x
        der = (func(x_o + h) - func(x_o - h)) / (2 * h)
        x = x_o - (func(x_o) / der)
        file.write("{:>3}         {:>10.20f} ".format(i, abs(x - copy)) + "\n")
        i += 1
    file.write("{:>3}         {:>10.20f} ".format(i, abs(x - copy)) + "\n")
    file.close()
    return x
