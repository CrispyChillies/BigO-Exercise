# Add to trie
# Find -> return the value of the last digit \

from queue import Queue

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
            return -1
        temp = temp.child[ch]
    return temp.countWord 

def findTrie(li, str):
    root = Node()

    for s in li:
        addword(root, s)
    res = findWord(root, str)
    return res

def removeWord(root, s, level, len):
    if root == None:
        return False
    if level == len:
        if root.countWord > 0:
            root.countWord -= 1
            return True
        return False
    ch = s[level]
    if ch not in root.child:
        return False
    flag = removeWord(root.child[ch], s, level + 1, len)
    if flag == True and root.child[ch].isalpha() == False and root.child[ch].isEmpty() == True:
        del root.child[ch]
    return flag

T = int(input())
l = []
q = Queue()
cnt = 1
for _ in range(T):
    n = int(input())

    for _ in range(n):
        s = input()
        l.append(s)
        q.put(s)
    
    checkTrie = False
    while not q.empty():
        check = q.get()
        res = findTrie(l,check)
    
        if res != 1:
            checkTrie = True    
            break 
    
    if checkTrie:
         print(f"Case {cnt}: NO")
    else:
         print(f"Case {cnt}: YES")
    
    cnt += 1