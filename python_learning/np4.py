import numpy as np

matrix1 = np.array([[2, 4],[3, 7]])

matrix2 = np.array([[5,8],[9,6]])

print('Matrix-1 is \n', matrix1)

print('Matrix-2 is \n', matrix2)

product = np.dot(matrix1, matrix2)

print('Product of Matrix-1 and Matrix-2 is \n', product)