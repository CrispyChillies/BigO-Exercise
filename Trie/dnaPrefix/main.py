INF = 1e9

class Node:
    def __init__(self) -> None:
        self.maxValue = -1
        self.child = dict()
        self.countWord = 0

def addword(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.countWord += 1 


def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return 0
        temp = temp.child[ch]
    return temp.countWord 

def printWord(root, s):
    #if root.isalpha():
    #    print(s)
    for ch in root.child:
        printWord(root.child[ch], s + ch)

def findLongest(s):
    root = Node()
    minlength = INF
    minStr = ""
    for word in s:
        if len(word) < minlength:
            minlength = len(word)
            minStr = word
        addword(root, word)

    checkStr = ""
    checkFind = 0
    result = -INF

    for c in minStr:
        checkStr += c
        checkFind = findWord(root, checkStr)
        # print(checkFind)
        if checkFind != 0:
            result = max(result, len(checkStr) * checkFind)

    return result

l = []

T = int(input())
cnt = 1
for _ in range(T):
    n = int(input())
    for _ in range(n):
        q = input()
        l.append(q)
    result = findLongest(l)
    print(f"Case {cnt}: {result}")
    l.clear()
    cnt += 1



