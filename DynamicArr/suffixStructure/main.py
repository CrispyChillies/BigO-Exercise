s = input()
t = input()

cnt_s = [0] * 26
cnt_t = [0] * 26

for char in s:
    id = ord(char) - ord('a')
    cnt_s[id] += 1

for char in t:
    id = ord(char) - ord('a')
    cnt_t[id] += 1

need_tree = automaton = array = False

for i in range(26):
    if cnt_t[i] > cnt_s[i]:
        need_tree = True
    elif cnt_t[i] < cnt_s[i]:
        automaton = True

match = -1

for i in range(len(t)):
    index = s.find(t[i], match + 1)
    if index != -1:
        match = index
    else:
        array = True
        break
if need_tree: 
    print("need tree")
else:
    if array and automaton:
        print("both")
    else:
        if array:
            print("array")
        else:
            print("automaton")