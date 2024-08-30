import numpy as np

data1 = np.array([1, 2, 3, 4, 5, 6])
data2 = np.array([2, 8, 0, 7, 8, 0])

data = np.stack((data1, data2), axis =0)

print(data)

corelation_mtrix = np.corrcoef(data)

print(corelation_mtrix)