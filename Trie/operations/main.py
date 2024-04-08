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
            return False
        temp = temp.child[ch]
    return temp.countWord > 0


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

def printWord(root, s):
    #if root.isalpha():
    #    print(s)
    for ch in root.child:
        printWord(root.child[ch], s + ch)


if __name__ == '__main__':
    root = Node()
    addword(root, "the")
    addword(root, "then")
    addword(root, "bigo")

    print(findWord(root, "there"))
    print(findWord(root, "th"))
    print(findWord(root, "the"))

    removeWord(root, "bigo", 0, 4)
    removeWord(root, "the", 0, 3)
    removeWord(root, "then", 0, 4)


