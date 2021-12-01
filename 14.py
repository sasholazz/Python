from numpy import *
from math import *
import matplotlib.pyplot as plt

def euler(x, y):
    return x + math.cos(y/sqrt(3))

def euler_coshi(x, y):
    return x + math.sin(y/sqrt(2))

def method1(euler, x, y):
    h = 0.1
    x = 1.2
    y = 2.1
    xarr = ([])
    yarr = ([])
    for i in range (0, 10):
        x += h
        xarr.append([x])
        y += h* euler(x, y)
        yarr.append([y])
    plt.plot(xarr, yarr)
    plt.xlabel('х')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    return xarr, yarr

def method2(euler_coshi, x, y):
    h = 0.1
    x = 0.8
    y = 1.3
    xarr = ([])
    yarr = ([])
    for i in range (0, 10):
        x += h
        xarr.append([x])
       
        y += h/2 * (euler_coshi(x, y) + euler_coshi(x+h, euler_coshi(x, y)))
        yarr.append([y])
    plt.plot(xarr, yarr)
    plt.xlabel('х')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    return xarr, yarr

print(method1(euler, 1.2, 2.2))
print(method2(euler_coshi, 0.8, 1.8))
