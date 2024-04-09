class Node:
    def __init__(self) -> None:
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

n = int(input())

root = Node()

for _ in range(n):
    s = input()
    operation, content = s.split(" ")
    if operation == "add":
        addword(root, content)
    elif operation == "find":
        result = findWord(root, content)
        print(result)
        