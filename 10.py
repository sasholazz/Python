import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
x = [1.4,1.6,2,2.5,3.1]
y= [2.39,3.85,2.74,1.58,3.15]
spl = UnivariateSpline(x, y)
xs = linspace (0,3.15, 1000)
plt.plot(x,y,'ro', xs, spl(xs), 'g')
plt.title("Spline")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(x)
plt.grid()
plt.show()
