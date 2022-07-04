def bubble_sort(arrays):
    n = len(arrays)
    cambios=1
    for i in range(n):
        print(arrays)
        cambios = 0
        for j in range(0,n-1-i):
            if arrays[j] > arrays[j+1]:
                arrays[j], arrays[j+1] = arrays[j+1], arrays[j]

                cambios =1
            if cambios<1:
                break


arrayl=[100,200,50,300]
print(bubble_sort(arrayl))



