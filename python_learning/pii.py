def linear_search(students, search_name):
    for i in range(len(students)):
        if students[i] == search_name:
            return i
    return -1

n = int(input('Enter input size:'))

students = {}
print(f'Enter the {n} names')
for i in range(n):
  students[i] = input()
  

print('The input data is \n', students)
search_name = input('Enter the search name: ')

index = linear_search(students, search_name)

if index == -1:
    print(f'{search_name} was not found in the list')
else:
    print(f'{search_name} was found at position {index+1}')