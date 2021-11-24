import numpy as np 
def gauss (a,b):
    n = len (b)
    k = 0
    while k <=n-1:
        i = k+1
        while i<n:
            j = k 
            if a[i ,k] != 0.0:
                l = a[i ,k]/a[k ,k]
                a[i,k+1:n] - l *a[k,k+1:n]
                b[i] = b[i] - l *b[k]
                j += 1
            i += 1
        k += 1
    k= n-1
    while k> -1:
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
        k-=1
    print ('Check',np.linalg.solve(a,b))

    return b

print('Method of Gaus',gauss(np.matrix([[3,-5,3],[1,2,1],[2,7,-1]]),np.matrix([1],[4],[3])))
