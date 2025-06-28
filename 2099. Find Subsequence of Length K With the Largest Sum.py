import copy
from collections import Counter
from typing import List


def maxSubsequence1(self, nums: List[int], k: int) -> List[int]:
    x = []
    for i in range(len(nums)):
        x.append([nums[i], i])
    x.sort(key=lambda x: x[0])
    y = x[-k:]
    y.sort(key=lambda x: x[1])
    z = []
    for i in range(k):
        z.append(y[i][0])
    return z


def maxSubsequence2(self, nums: List[int], k: int) -> List[int]:
    x = sorted(nums)
    p = Counter(x[-k:])
    x = []
    y = 0
    for i in range(len(nums)):
        if (nums[i] in p and p[nums[i]] > 0):
            x.append(nums[i])
            p[nums[i]] -= 1
            y += 1
        if (y == k):
            break
    return x
nums = [2,1,3,3]
k = 2
print(maxSubsequence1(0,nums, k))
print(maxSubsequence2(0,nums, k))