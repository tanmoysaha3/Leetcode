def answerString(self, word: str, numFriends: int) -> str:
    n = len(word)
    if (numFriends == 1):
        return word
    p = word[0]
    q = [0]
    for i in range(n):
        if (word[i] > p):
            p = word[i]
            q = [i]
        elif (word[i] == p):
            q.append(i)
    z = word[q[0]:q[0] + n - numFriends + 1]
    for i in range(1, len(q)):
        b = word[q[i]:q[i] + n - numFriends + 1]
        if (b > z):
            z = b
    return z


word = "nbjnc"
numFriends = 2
answerString(0,word, numFriends)