sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89,10,23,45,23]
iteraciones=(len(sample_list)//3)

chunk=len(sample_list)//3
start=0
end=chunk

for i in range(iteraciones):
    indexes=slice(start,end)
    list_chunk=sample_list[indexes]
    #reverse
    print(list(reversed(list_chunk)))
    start=end
    end+=chunk
    


#slice(start,stop,step)
