from numpy import *
import matplotlib.pyplot as plt
def sd(x):
    return 5*sin(10*x)*sin(3*x)
x = linspace(0, 3, 51)
y = sd(x)
plt.plot(x, y, 'g--', label='5*sin(10*x)*sin(3*x)')
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
