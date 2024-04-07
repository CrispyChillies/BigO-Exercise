class Node:
    def __init__(self) -> None:
        self.maxValue = -1
        self.child = dict()

def addWord(root, s, w):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.maxValue(temp.maxValue, w)
    
def getMaxValue(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return -1
        temp = temp.child[ch]
    return temp.maxValue

if __name__ == '__main__':
    n,q = map(int, input().split())
    root = Node()
    for _ in range(n):
        word, weight = map(str, input().split())
        weight = int(weight)
        addWord(root, word, weight)
    for _ in range(q):
        query = input()
        print(getMaxValue(root, query))
