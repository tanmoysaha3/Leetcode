from typing import List

def triangleType(self, nums: List[int]) -> str:
    nums.sort()
    if (nums[0] + nums[1] <= nums[2]):
        return "none"
    else:
        n = len(set(nums))
        if (n == 1):
            return "equilateral"
        elif (n == 2):
            return "isosceles"
        else:
            return "scalene"

nums = [3,4,5]
print(triangleType(0,nums))