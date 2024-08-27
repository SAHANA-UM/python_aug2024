def binary_search(names, search_name):
    start_index = 0
    end_index = len(names) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if names[mid_index] == search_name:
            return mid_index
        elif names[mid_index] > search_name:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

n = int(input('Enter input size: '))

names = []
print(f'Enter the {n} names')
for i in range(n):
    names.append(input())

print('The input data is \n', names)
search_name = input('Enter the search name: ')

index = binary_search(names, search_name)
if index == -1:
    print(f'{search_name} was not found in the list')
else:
    print(f'{search_name} was found')
    
