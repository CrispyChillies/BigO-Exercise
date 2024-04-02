def binarySearch(arr, start,  x):
    low = start + 1
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1


T = int(input())

for _ in range(T):

    n,m = map(int, input().split())

    friend = list(map(int, input().split()))
    friend.sort()
        
    pairs = 0
    
    # Don't use 'in [list]' to check inside cause it will cause alot

    checkPair = set()

    for i in range(n):
        pay = m - friend[i]

        if pay not in checkPair:

            enough = binarySearch(friend, i, pay)

            if enough != -1:
                checkPair.add(pay)
                checkPair.add(friend[i])
                pairs += 1

    print(pairs)
    