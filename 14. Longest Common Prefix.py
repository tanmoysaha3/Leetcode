from typing import List

strs = ["flower","flow","flight"]
def longestCommonPrefix1(self, strs: List[str]) -> str:
    strs = list(set(strs))
    strs.sort()
    i = min(len(s) for s in strs)
    for i in range(i):
        if (strs[0][i] != strs[-1][i]):
            i -= 1
            break
    return strs[0][:i + 1]

print(longestCommonPrefix1(0,strs))


def longestCommonPrefix2(self, strs: List[str]) -> str:
    min_length = min(len(s) for s in strs)
    strs.sort()
    x = 0
    for i in range(min_length):
        if (strs[0][i] == strs[-1][i]):
            x += 1
        else:
            break
    return strs[0][:x]

print(longestCommonPrefix2(0,strs))