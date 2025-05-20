from collections import defaultdict
from typing import List


def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    x = defaultdict(int)
    y = defaultdict(int)
    for i in queries:
        x[i[0]] += 1
        y[i[1]] += 1
    z = 0
    for i in range(len(nums)):
        z += x.get(i, 0)
        if (z < nums[i]):
            return False
        z -= y.get(i, 0)

    return True

nums = [4,3,2,1]
queries = [[1,3],[0,2]]
print(isZeroArray(0,nums,queries))