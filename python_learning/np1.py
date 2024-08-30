import numpy as np

array1 = np.zeros((1,4))

print (array1)
print(type(array1))
for row in array1:
    print(type(row))
    for element in row:
        print(type(element))
        print(element)