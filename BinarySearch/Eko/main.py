# INF = -1e9

# def getWood(arr, cut):
#     totalWood = 0

#     for i in range(len(arr)):
#         if arr[i] > cut:
#             totalWood += arr[i] - cut
#     return totalWood
        

# def binarySearch(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#     print(arr)
#     max = (INF, INF)
 
#     while low <= high:
 
#         mid = (high + low) // 2
 
#         # If x is greater, ignore left half
#         if getWood(heights, arr[mid]) > x:
#             low = mid + 1
 
#         # If x is smaller, ignore right half
#         elif getWood(heights, arr[mid]) < x:
#             high = mid - 1
 
#         # means x is present at mid
#         else:
#             return mid
            
#     # If we reach here, then the element was not present
#     return -1



# n, m = map(int, input().split())

# heights = list(map(int, input().split()))
# heights.sort()

# mid = len(heights) // 2

# wood = getWood(heights, heights[mid])


# ans = 0

# if wood == m:
#     print(heights[mid])
# elif wood > m:
#     segment = range(heights[mid], heights[len(heights) - 1])
#     arr = list(segment)
#     ans = binarySearch(arr, m)
# else:
#     segment = range(0,heights[mid])
#     arr = list(segment)
#     ans = binarySearch(arr, m)


# print(ans)


def calculate_wood_cut(heights, cut_height):
    total_wood = 0
    for height in heights:
        if height > cut_height:
            total_wood += height - cut_height
    return total_wood

def find_max_height(heights, required_wood):
    max_height = max(heights)  # Start with the maximum tree height
    min_height = 0              # Min height to cut wood
    result_height = 0

    while min_height <= max_height:
        mid = (min_height + max_height) // 2
        wood_cut = calculate_wood_cut(heights, mid)
        
        if wood_cut >= required_wood:
            result_height = mid
            min_height = mid + 1
        else:
            max_height = mid - 1

    return result_height

# Input
N, M = map(int, input().split())
tree_heights = list(map(int, input().split()))

# Output
print(find_max_height(tree_heights, M))
