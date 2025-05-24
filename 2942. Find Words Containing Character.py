from typing import List


def findWordsContaining(self, words: List[str], x: str) -> List[int]:
    z = []
    for i in range(len(words)):
        if (x in words[i]):
            z.append(i)
    return z

words = ["leet","code"]
x = "e"
print(findWordsContaining(0,words,x))