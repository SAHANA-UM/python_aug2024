def insertion_sort(array):
    for i in range(1, len(array)):
       element = array[i]
       j = i - 1
       while j >= 0 and array[j] > element:
           array[j+1] = array[j]
           j = j - 1
       array[j+1] = element
    return array
        
n = int(input('Enter input size: '))

array = []
print(f'Enter the {n} elements:')
for i in range(n):
    array.append(input())

print('The array before the insertionsort: ')

for i in range(n):
    print(array[i], end=' ')

array = insertion_sort(array)

print('\nThe array after the insertionsort: ')

for i in range(n):
    print(array[i], end=' ')
    


