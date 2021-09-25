import numpy as np

m1 = np.array([[2, 5],[4, 7]])
m2 = np.array([[4, 7], [6, 2]])

sum = m1 + m2
print("Addition of matrix  : \n",sum) 

multi = m1.dot(m2)
print("multiplication of matrix : \n",multi)

trans = m1.transpose()
print("Transpose of Matrix : \n",trans)