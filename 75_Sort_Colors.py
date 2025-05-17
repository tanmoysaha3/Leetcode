from collections import Counter
from typing import List

nums = [2,0,2,1,1,0]

def sortColors(self, nums: List[int]) -> None:
    c = dict(Counter(nums))
    b = [0, 1, 2]
    a = 0
    for i in range(3):
        for j in range(c.get(i, 0)):
            nums[a] = b[i]
            a += 1

print(sortColors(0,nums))