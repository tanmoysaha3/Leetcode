from typing import List


def partitionArray(self, nums: List[int], k: int) -> int:
    nums = list(set(nums))
    nums.sort()
    x = 0
    y = nums[0]
    for i in range(1, len(nums)):
        if (nums[i] - y > k):
            y = nums[i]
            x += 1
    return x + 1

nums = [3,6,1,2,5]
k = 2
print(partitionArray(0,nums, k))
