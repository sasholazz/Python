import math
from scipy import optimize 
x0=-1.1
y=-1
def f1(y):
    return -1.2 + math.sin(y+1)-x 
def f2(x):
    return 2 - 2*y + math.cos(x)
def iter (x,y,e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e)&(abs(yn1-yn)>=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
        print ('Simple iteration:')
        print ('xn',xn,'yn=',yn,'The amount of iteration = ',n)
iter(x0,y0,0.0001)
def f(x):
    return math.sin(y[1]+1) - x[0] - 1.2, math.cos(x[0]) + 2*y - 2
s = optimize.root(f, [0,0], method = 'hybr')
