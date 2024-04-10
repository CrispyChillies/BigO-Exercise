# Add to trie
# Find -> return the value of the last digit \

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

T = int(input())
l = []
cnt = 1

for _ in range(T):
    n = int(input())
    root = Node()

    for _ in range(n):
        s = input()
        l.append(s)
        addword(root, s)
    
    checkTrie = False
    for word in l:
        res = findWord(root, word)
        if res > 1:
            checkTrie = True
            print(word)
            break
        
    if checkTrie:
         print(f"Case {cnt}: NO")
    else:
         print(f"Case {cnt}: YES")
    
    cnt += 1