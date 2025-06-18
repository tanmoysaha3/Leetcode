from typing import List


def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    nums.sort()
    y=[]
    for i in range(0,len(nums),3):
        if(nums[i+2]-nums[i]<=k):
            y.append(nums[i:i+3])
        else:
            y=[]
            break
    return y

nums = [2,4,2,2,5,2]
k = 2
print(divideArray(0,nums, k))