import numpy as np

A = np.array([[1, 2], [4, -1]])
B = np.array([[2, -3], [-4, 1]])
C = A-B
print(C)

# 2
a = np.array([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])
result = np.linalg.matrix_power(a, 2)
print(result)



# 3
A = np.array([[3, 5], [2, 1]])
B = np.array([[6, -1], [-3, 2]])
C = A.dot(B)
print(C)

# 4 
A = np.matrix([[2, 3 ,4], [1, 0 ,6], [7, 8 ,9]])
print(A)
print(A.T)
det_A = round(np.linalg.det(A), 3)
det_A_t = round(np.linalg.det(A.T), 3)
print(det_A)
print(det_A_t)
#5
A = np.matrix([[1, 2, 3, 4], [-2, 1, -4, 3], [3, -4, 1, 2], [4, 3, -2, -1]])
print(A)
print(A.T)
det_A = round(np.linalg.det(A), 3)
det_A_t = round(np.linalg.det(A.T), 3)
print(det_A)
print(det_A_t)

#6
A = np.matrix([[1, 2, -3], [0, 1, 2], [0, 0, 1]])
A_inv = np.linalg.inv(A)
print(A_inv)

#7

A = np.matrix([[1, 2,3 ,4],[3 ,-1, 2 ,5],[1 ,2 ,3 ,4],[1 ,3 ,4 ,5]])
np.linalg.matrix_rank(A)
print(A)
