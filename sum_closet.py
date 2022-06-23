#return the sum of three numbers that is closet to the num 
target = 2
nums=[-1,2,1,-4]

#como ordenamos una lista
print(sorted(nums,reverse=True))
print(sorted(nums))

#basically we have a pointer over there 

#we begin with corner cases
if len(nums) < 3:
    return([])
triplets=[]

#solution with sorting 
nums2=sorted(nums)

for i in range (0,len(nums)-2):
    
    if nums2[i] > 0:
        break
    if nums2[i] == nums2[i-1] and i > 0:
        continue
    lower = i +1
    upper = len(nums)-1
    
    while lower < upper:
        s=