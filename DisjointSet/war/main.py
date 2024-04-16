parent = []
ranks = []

def makeSet(MAX):
    global parent, ranks, nums
    parent = [i for i in range(MAX + 5)]
    ranks = [0 for i in range(MAX + 5)]
    nums = [1 for i in range(MAX + 5)]



if __name__ == "__main__":
    n = int(input())
    makeSet(n)
    c, x, y = map(int, input().split())
    n = int(input())