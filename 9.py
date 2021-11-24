import numpy as np
import math
 
mas_x=[0.15, 0.16, 0.17, 0.18, 0.19, 0.20,0.21,0.22,0.23,0.24,0.25]
mas_y=[4.4817 ,4.9530, 5.4739, 6.0496, 6.6859, 7.3891,8.1662,9.0250,9.9742,11.0232,12.1825]
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
