from typing import List
nums=[2,7,11,15]
target = 9

#this is the intuitive solution that almost always is not too fast 
""" def twoSum( nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
                         """
#print(twoSum(nums,target))

#this is the no intuitive solution that i going to try 
def twoSum(nums,target):
    mapa={}
    for i in nums:
        if i not in mapa:
            mapa[i]==i
        if target - i in mapa:
            return [mapa[i],i]
print(twoSum(nums,target))
        