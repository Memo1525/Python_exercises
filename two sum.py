#no olvidar los casos esquina
#brute force solution

def sumatoria(nums):
    if len(nums) < 3: #aqui se trata el caso esquina
        return ([])
    triplets=[]
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if (nums[i]+ nums[j] + nums[k]) == 0:
                    triplets.append((tuple(sorted([nums[i],nums[j],nums[k]]))))
    return list(set(triplets))



print(sumatoria([-1,0,1,2,-1,-4,2,3,4,1,-1,-1,-1,-1,345,-346]))


