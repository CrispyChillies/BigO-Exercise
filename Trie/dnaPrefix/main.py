import itertools

ALPHABET_SIZE = 26
indexs = 0
class TrieNode:
	# constructor
	def __init__(self):
		self.isLeaf = False
		self.children = [None]*ALPHABET_SIZE    

def insert(key, root):
	pCrawl = root
	for level in range(len(key)):
		index = ord(key[level]) - ord('A')
		if pCrawl.children[index] == None:
			pCrawl.children[index] = TrieNode()
		pCrawl = pCrawl.children[index]
	pCrawl.isLeaf = True

def constructTrie(arr, n, root):
	for i in range(n):
		insert(arr[i], root)

def countChildren(node):
	count = 0
	for i in range(ALPHABET_SIZE):
		if node.children[i] != None:
			count +=1
			# Keeping track of diversion in the trie
			global indexs
			indexs = i
	return count
	

def walkTrie(root):
	pCrawl = root
	prefix = ""
	while(countChildren(pCrawl) == 1 and pCrawl.isLeaf == False):
		pCrawl = pCrawl.children[indexs]
		prefix += chr(97 + indexs)
	return prefix or ""

def commonPrefix(arr, n, root):
	constructTrie(arr, n, root)
	return walkTrie(root)

def findLongestPrefixSubset(arr, n):
    result = -1
    for i in range(n):
        combinations = list(itertools.combinations(arr, i + 1))
        for combination in combinations:
            root = TrieNode()
            result = max(result, len(commonPrefix(combination,i + 1, root)) * len(combination))
    
    return result

T = int(input())
arr = []
cnt = 1
for _ in range(T):
	n = int(input())
	for _ in range(n):
		q = input()
		arr.append(q)
	res = findLongestPrefixSubset(arr,len(arr))
	print(f"Case {cnt}: {res}")
	arr.clear()
	cnt += 1




