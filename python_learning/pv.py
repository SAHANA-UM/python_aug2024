n = int(input('Enter size of array: '))

original_array = []

print(f'Enter {n} elements of the Original Array')
for i in range(n):
	original_array.append(int(input()))

m = int(input('Enter size of transported array: '))

transported_array = list()
print(f'Enter {m} elements of the transported Array')
for i in range(m):
	transported_array.append(int(input()))

original_array.sort()
transported_array.sort()

print(original_array)
print(transported_array)

missing_elements_array = []
j = 0

if m == 0:
	missing_elements_array = original_array
else:
	for i in range(len(original_array)):
		if original_array[i] == transported_array[j]:
			j += 1
		else:
			missing_elements_array.append(original_array[i])
		if j == m and i != n-1:
			missing_elements_array.extend(original_array[i+1:])
			break
		
print('Missing elements are: ', set(missing_elements_array))
