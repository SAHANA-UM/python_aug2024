def partition_array(array):
    pivot=array[-1] 
    j=0 
    for i in range(len(array)-1): 
        if array[i]<pivot:
            array[j], array[i]=array[i], array[j] 
            j += 1 
    array[j],array[-1] = array[-1],array[j]
array=[12,4,19,23,8,7,20,15,5,13] 
print(array) 
partition_array(array) 
print(array)