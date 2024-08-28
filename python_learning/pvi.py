def bubble_sort(array):
    count = 0
    for i in range( 0 , n-1):
        sorted = True # Assume the array is sorted
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        count += 1
    print ('count = ',count)           
        
n = int(input('Enter input size: '))

array = []
print(f'Enter the {n} elements:')
for i in range(n):
    array.append(input())
bubble_sort(array)

print('\nThe array after the bubblesort: ')
for i in range(n):
    print(array[i], end=' ')

    