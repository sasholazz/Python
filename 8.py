import numpy as np
import math

mas_x=[0, 0.1, 0.2, 0.3, 0.4, 0.5]
mas_y=[1.2733 ,1.8007, 2.3606, 2.9577, 3.5969, 4.2833]
h = mas_x[1] - mas_x[0]
k=0
def y(mas_y,j):
    mas=[]
    for i in range(len(mas_y)):
        mas.append(mas_y[i] - mas_y[i-1])
    mas.pop(0)  
    if j == 1:
        return mas
    else:
        j-=1
        return y(mas, j)
yx1=1/h*((y(mas_y, 1)[1])-(y(mas_y, 2)[1])/2+(y(mas_y, 3)[1])/3-(y(mas_y, 4)[1])/4)
yx2=1/h**2*((y(mas_y, 2)[1])-(y(mas_y, 3)[1])+11/12*(y(mas_y, 4)[1]))
print(y(mas_y, 3))
print (yx1)
print (yx2)
