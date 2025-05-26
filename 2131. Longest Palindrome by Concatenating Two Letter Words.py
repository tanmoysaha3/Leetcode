from collections import Counter
from typing import List


def longestPalindrome(self, words: List[str]) -> int:
    m = Counter(words)
    x, y, r = 0, 0, 0
    for i in m:
        if (i[0] == i[1]):
            if (m[i] % 2 == 1):
                x += m[i] - 1
                r = 1
            else:
                x += m[i]
        else:
            if (i[::-1] in m):
                y += min(m[i], m[i[::-1]])

    return y * 2 + x * 2 + r * 2

words = ["ab","ty","yt","lc","cl","ab"]
print(longestPalindrome(0,words))
