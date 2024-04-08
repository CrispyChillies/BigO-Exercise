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
            return False
        temp = temp.child[ch]
    return temp.countWord > 0

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
    # print(operation)
    # print(content)

# n = int(input())
# code = []

# for _ in range(n):
#     s = input()
#     operation, content = s.split(" ")
#     if operation == "add":
#         code.append(content)
#     elif operation == "find":
#         cnt = 0
#         for c in code:
#             if content in c:
#                 cnt += 1
#         print(cnt)
