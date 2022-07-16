def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        # Last i elements are already in place 
        for j in range(0, n-i-1):  #los ultimos 2 ya estan en su lugar 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


arrayl=[100,200,50,300]
print(bubbleSort(arrayl))



